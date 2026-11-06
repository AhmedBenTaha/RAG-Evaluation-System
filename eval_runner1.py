from RAG1.agent import Ask
import json


with open("eval_dataset_jsonl","r") as f:
    test_cases = [json.loads(line) for line in f]


    results = []
    for test_case in test_cases:
        
        question = test_case["question"]
        expected_answer = test_case["expected_answer"]
        print(f"Question: {question}")
        rag_result = Ask(question)
        
        result = {
            "question": question,
            "expected_answer": expected_answer,
            "actual_answer": rag_result["answer"],
            "context": rag_result["context"]
        }
        results.append(result)
        print(f"Answer: {rag_result['answer']}")

with open("results1.jsonl", "w", encoding="utf-8") as file:
    for result in results:
        file.write(json.dumps(result)+"\n")

print("\nDone! Results1 saved to results1.jsonl")