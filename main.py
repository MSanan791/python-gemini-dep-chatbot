
from agent_logic import create_graph

if __name__ == "__main__":
    app = create_graph()
    final_result = app.invoke({})
    print("\n📋 Diagnosis Summary:")
    print(final_result["diagnosis"])
