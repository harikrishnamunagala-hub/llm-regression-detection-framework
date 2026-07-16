from src.datasets import load_dataset
from src.models import GeminiModel,MockModel
from src.evaluator import Evaluator
from src.regression import Regression_Detector
from src.report import Report_Generator
from src.config import ConfigLoader
from src.model_factory import ModelFactory
from src.logger import logger


def main():
    
    logger.info("Loading configuration...")
    config = ConfigLoader.load_config("config/config.yaml")
    
    logger.info("Loading dataset...")
    dataset = load_dataset(config["dataset_path"])

    logger.info("Creating baseline model...")
    baseline_model = ModelFactory.create_model(
    config["baseline"]["provider"],
    "baseline",
    config["baseline"]["model"]
    )

    logger.info("Creating candidate model...")
    candidate_model = ModelFactory.create_model(
    config["candidate"]["provider"],
    "candidate",
    config["candidate"]["model"]
    )

    baseline_evaluator = Evaluator(baseline_model)
    candidate_evaluator = Evaluator(candidate_model)

    logger.info("Evaluating baseline model...")
    baseline_evaluation=baseline_evaluator.evaluate(dataset)

    logger.info("Evaluating candidate model...")
    candidate_evaluation=candidate_evaluator.evaluate(dataset)

    baseline_results=baseline_evaluation
    candidate_results=candidate_evaluation

    '''for result in results:
        print("=" * 60)
        print(f"Question : {result['question']}")
        print(f"Expected : {result['expected_answer']}")
        print(f"Generated: {result['generated_answer']}")
        print(f"Score:{result['score']}")
        print()'''
    
    detector=Regression_Detector()
    logger.info("Detecting regression...")

    report_generator=Report_Generator()

    
    regression_report = detector.detect(
    baseline_results["accuracy"],
    candidate_results["accuracy"],
    config["regression_threshold"]
    )

    logger.info("Generating report...")
    report_generator.generate_report(
    baseline_evaluation,
    candidate_evaluation,
    regression_report,
    config
    )

    logger.info("Evaluation completed successfully.")


    '''print("=" * 60)
    print(f"Correct Answers : {evaluation['correct_answers']}")
    print(f"Total Questions : {evaluation['total_questions']}")
    print(f"Accuracy        : {evaluation['accuracy']:.2f}%")
    print("=" * 60)'''

    print("="*60)
    print(f"Baseline Accuracy : {baseline_results['accuracy']:.2f}%")
    print(f"Candidate Accuracy: {candidate_results['accuracy']:.2f}%")
    print(f"Baseline Avg Latency : {baseline_evaluation['average_latency']:.4f} sec\n")
    print(f"Candidate Avg Latency : {candidate_evaluation['average_latency']:.4f} sec\n")
    print(f"Accuracy Drop     : {regression_report['drop']:.2f}%")
    print(f"Status            : {regression_report['status']}")
    print("="*60)

if __name__ == "__main__":
    main()