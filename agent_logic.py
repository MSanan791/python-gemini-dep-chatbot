from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import RetrievalQA
from langgraph.graph import StateGraph, END

from embeddings import load_vectorstore
from prompts.phq_gad_template import PHQ9_QUESTIONS, GAD7_QUESTIONS

import os
from dotenv import load_dotenv
from pydantic import BaseModel
from typing import Dict, List, Tuple

load_dotenv()

# Define the state schema for the StateGraph
from typing import Optional, Any

class StateSchema(BaseModel):
    responses: Dict[str, List[Tuple[str, str]]] = {}
    diagnosis: Optional[Any] = None  # Add this line


llm = ChatGoogleGenerativeAI(
    model="models/gemini-1.5-flash-latest",   # ✅ FULL name
    temperature=0.3,
    google_api_key=os.getenv("GEMINI_API_KEY")
)


retriever = load_vectorstore().as_retriever(search_kwargs={"k": 4})
qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

def map_response(text):
    mapping = {
        "not at all": 0,
        "no": 0,
        "several days": 1,
        "a little": 1,
        "more than half the days": 2,
        "yes": 2,
        "nearly every day": 3,
        "always": 3
    }
    return mapping.get(text.lower().strip(), None)

def ask_questions(state):
    import os
    test_mode = os.getenv("TEST_MODE", "0") == "1"

    responses = {"PHQ9": [], "GAD7": []}

    if test_mode:
        from test_input import PHQ9_RESPONSES, GAD7_RESPONSES
        for q, score in PHQ9_RESPONSES:
            responses["PHQ9"].append((q, str(score)))
        for q, score in GAD7_RESPONSES:
            responses["GAD7"].append((q, str(score)))
        return {"responses": responses}

    # Default manual input
    for q in PHQ9_QUESTIONS:
        while True:
            print(f"[PHQ-9] {q}")
            print("Your options: not at all, several days, more than half the days, nearly every day")
            user_input = input("> ")
            score = map_response(user_input)
            if score is not None:
                responses["PHQ9"].append((q, str(score)))
                break
            else:
                print("❌ Invalid input. Please type one of the listed options.")

    for q in GAD7_QUESTIONS:
        while True:
            print(f"[GAD-7] {q}")
            print("Your options: not at all, several days, more than half the days, nearly every day")
            user_input = input("> ")
            score = map_response(user_input)
            if score is not None:
                responses["GAD7"].append((q, str(score)))
                break
            else:
                print("❌ Invalid input. Please type one of the listed options.")

    return {"responses": responses}

def analyze(state):


    user_inputs = state.responses
    analysis_result = qa_chain.invoke(
        f"Based on these PHQ-9 and GAD-7 responses: {user_inputs}, determine if the patient likely has depression, anxiety, both, or neither."
    )


    # Return a merged state dict containing both responses and diagnosis
    return {"diagnosis": analysis_result}


def create_graph():
    graph = StateGraph(state_schema=StateSchema)  # Pass schema here!
    graph.add_node("ask", ask_questions)
    graph.add_node("analyze", analyze)
    graph.set_entry_point("ask")
    graph.add_edge("ask", "analyze")
    graph.add_edge("analyze", END)
    return graph.compile()
