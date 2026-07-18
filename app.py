from src.datasets import load_dataset
from src.models import GeminiModel,MockModel
from src.evaluator import Evaluator
from src.regression import Regression_Detector
from src.report import Report_Generator
from src.config import ConfigLoader
from src.model_factory import ModelFactory
from src.logger import logger
from src.scorers.scorer_factory import ScorerFactory
from src.prompt_loader import PromptLoader
from src.history import HistoryManager
from src.drift_detector import DriftDetector
from src.html_report import HTMLReportGenerator
from src.slack_notifier import SlackNotifier
import os

def main():
    
    logger.info("Loading configuration...")
    config = ConfigLoader.load_config("config/config.yaml")

    os.makedirs(os.path.dirname(config["report_path"]), exist_ok=True)
    os.makedirs(os.path.dirname(config["html_report_path"]), exist_ok=True)
    os.makedirs(os.path.dirname(config["history_path"]), exist_ok=True)
    
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
    
    baseline_prompt = PromptLoader.load_prompt(
    config["baseline"]["prompt"]
    )

    candidate_prompt = PromptLoader.load_prompt(
    config["candidate"]["prompt"]
    )


    scorer=ScorerFactory.create_scorer(config["scorer"])
    baseline_evaluator = Evaluator(baseline_model,scorer,baseline_prompt)
    candidate_evaluator = Evaluator(candidate_model,scorer,candidate_prompt)

    logger.info("Evaluating baseline model...")
    baseline_evaluation=baseline_evaluator.evaluate(dataset)

    logger.info("Evaluating candidate model...")
    candidate_evaluation=candidate_evaluator.evaluate(dataset)

    baseline_results=baseline_evaluation
    candidate_results=candidate_evaluation
    
    detector=Regression_Detector()
    notifier = SlackNotifier()
    logger.info("Detecting regression...")

    report_generator=Report_Generator()

    
    regression_report = detector.detect(
    baseline_evaluation,
    candidate_evaluation,
    config["regression_threshold"]
    )

    logger.info("Generating report...")
    report_generator.generate_report(
    baseline_evaluation,
    candidate_evaluation,
    regression_report,
    config
    )

    html_report = HTMLReportGenerator()

    html_report.generate(
    baseline_evaluation,
    candidate_evaluation,
    regression_report,
    config
    )
    
    history = HistoryManager()

    history.save_run(
    baseline_evaluation,
    candidate_evaluation,
    regression_report,
    config
    )
    
    drift_detector = DriftDetector()

    drift_report = drift_detector.detect_drift(
    window=config["drift"]["window"],
    threshold=config["drift"]["threshold"]
    )

    print("\nDrift Detection")
    print("=" * 60)
    print(f"Status          : {drift_report['status']}")
    print(f"Average Accuracy: {drift_report['average_accuracy']}")
    print(f"Latest Accuracy : {drift_report['latest_accuracy']}")
    print(f"Drop            : {drift_report['drop']}%")
    print("=" * 60)

    logger.info("Evaluation completed successfully.")

    print("="*60)
    print(f"Baseline Accuracy : {baseline_results['accuracy']:.2f}%")
    print(f"Candidate Accuracy: {candidate_results['accuracy']:.2f}%")
    print(f"Regressions      : {regression_report['regressions']}")
    print(f"Improvements     : {regression_report['improvements']}")
    print(f"Baseline Avg Latency : {baseline_evaluation['average_latency']:.4f} sec\n")
    print(f"Candidate Avg Latency : {candidate_evaluation['average_latency']:.4f} sec\n")
    print(f"Accuracy Drop     : {regression_report['drop']:.2f}%")
    print(f"Status            : {regression_report['status']}")
    print("="*60)
    
    if regression_report["status"] == "FAIL":
        notifier.send(
            baseline_evaluation,
            candidate_evaluation,
            regression_report
        )

    return {
        "baseline_evaluation": baseline_evaluation,
        "candidate_evaluation": candidate_evaluation,
        "regression_report": regression_report,
        "drift_report": drift_report
    }    

if __name__ == "__main__":
    main()