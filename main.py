from agent_logic import create_graph

def pretty_print_diagnosis(text):
    # Example: Replace \n\n with single newline for compactness
    cleaned = text.replace("\n\n", "\n").strip()
    print("🧠 Mental Health Screening Result:")
    print("-------------------------------")
    print(cleaned)
    print("-------------------------------")


if __name__ == "__main__":
    app = create_graph()
    final_result = app.invoke({})

    diagnosis = final_result.get("diagnosis")
    if diagnosis and "result" in diagnosis:
        if diagnosis and "result" in diagnosis:
            pretty_print_diagnosis(diagnosis["result"])
        else:
            print("⚠️ Diagnosis result not available.")

    else:
        print("⚠️ Diagnosis result not available.")

