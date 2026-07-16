from src.scorer import Scorer
import time

class Evaluator:
    def __init__(self,model):
        self.model=model
        self.scorer=Scorer()

    def evaluate(self,dataset):
        results=[]
        for sample in dataset:
            
            try:
                
                start_time=time.perf_counter()
                answer = self.model.generate(sample["question"])
                end_time=time.perf_counter()
                latency=end_time-start_time
                score = self.scorer.score(
                sample["expected_answer"],
                answer
                )

            except Exception as e:

                answer = f"ERROR: {str(e)}"
                score = 0
                latency=0

            results.append({
                "id": sample['id'],
                "question": sample['question'],
                "expected_answer": sample['expected_answer'],
                "generated_answer": answer,
                "score":score,
                "latency":latency
            })

        total_questions=len(results)
        correct_answers=sum(result["score"] for result in results)
        accuracy=(correct_answers/total_questions)*100
        average_latency=sum(result["latency"] for result in results)/total_questions

        return {
            "results":results,
            "accuracy":accuracy,
            "average_latency":average_latency,
            "correct_answers": correct_answers,
            "total_questions": total_questions,
        }   