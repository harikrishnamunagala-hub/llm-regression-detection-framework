import json
import os
from datetime import datetime


class HistoryManager:

    def __init__(self, path="history/evaluation_history.json"):

        self.path = path

        if not os.path.exists(self.path):
            with open(self.path, "w") as file:
                json.dump([], file)

    def save_run(
        self,
        baseline,
        candidate,
        regression,
        config
    ):

        history = self.load_history()

        history.append({

            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),

            "baseline_provider": config["baseline"]["provider"],

            "candidate_provider": config["candidate"]["provider"],

            "baseline_model": config["baseline"]["model"],

            "candidate_model": config["candidate"]["model"],

            "baseline_accuracy": baseline["accuracy"],

            "candidate_accuracy": candidate["accuracy"],

            "baseline_latency": baseline["average_latency"],

            "candidate_latency": candidate["average_latency"],

            "status": regression["status"],

            "accuracy_drop": regression["drop"],

            "regressions": regression["regressions"],

            "improvements": regression["improvements"]

        })

        with open(self.path, "w") as file:
            json.dump(history, file, indent=4)

    def load_history(self):

        try:

            with open(self.path, "r") as file:
                return json.load(file)

        except (json.JSONDecodeError, FileNotFoundError):

            return []