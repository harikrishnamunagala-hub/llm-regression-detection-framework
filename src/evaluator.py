from src.scorers import base_scorer
import time

class Evaluator:
    def __init__(self,model,scorer:base_scorer,prompt):
        self.model=model
        self.scorer=scorer
        self.prompt=prompt
        

    def evaluate(self,dataset):
        results=[]
        for sample in dataset:
            
            try:
                
                start_time=time.perf_counter()
                answer = self.model.generate(sample["question"],self.prompt)
                end_time=time.perf_counter()
                latency=end_time-start_time
                evaluation = self.scorer.score(
                sample["expected_answer"],
                answer
                )
                

            except Exception as e:

                answer = f"ERROR: {str(e)}"
                latency = 0

                evaluation = {
                "passed": False,
                "metric_score": 0,
                "metric": "ERROR",
                "threshold": 0
                }

            results.append({
                "id": sample['id'],
                "question": sample['question'],
                "expected_answer": sample['expected_answer'],
                "generated_answer": answer,
                "passed": evaluation["passed"],
                "metric_score": evaluation["metric_score"],
                "metric": evaluation["metric"],
                "threshold": evaluation["threshold"],
                "latency":latency
            })

        total_questions=len(results)
        correct_answers=sum(result["passed"] for result in results)
        failed_answers = total_questions - correct_answers

        pass_rate = (correct_answers / total_questions) * 100

        average_metric_score = (
        sum(result["metric_score"] for result in results)
        / total_questions
        )
        accuracy=(correct_answers/total_questions)*100
        average_latency=sum(result["latency"] for result in results)/total_questions

        return {
            "results": results,

            "accuracy": accuracy,

            "pass_rate": pass_rate,

            "average_metric_score": average_metric_score,

            "average_latency": average_latency,

            "correct_answers": correct_answers,

            "failed_answers": failed_answers,

            "total_questions": total_questions,
            }   