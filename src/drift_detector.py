import json


class DriftDetector:

    def __init__(self, history_path="history/evaluation_history.json"):
        self.history_path = history_path

    def detect_drift(self, window=5, threshold=3):

        with open(self.history_path, "r") as file:
            history = json.load(file)

        if len(history) < window + 1:
            return {
                "drift": False,
                "status": "Not Enough Data",
                "average_accuracy": None,
                "latest_accuracy": None,
                "drop": 0
            }

        recent_runs = history[-(window + 1):-1]

        latest_run = history[-1]

        average_accuracy = sum(
            run["candidate_accuracy"] for run in recent_runs
        ) / window

        latest_accuracy = latest_run["candidate_accuracy"]

        drop = average_accuracy - latest_accuracy

        return {
            "drift": drop >= threshold,
            "status": "Drift Detected" if drop >= threshold else "Stable",
            "average_accuracy": round(average_accuracy, 2),
            "latest_accuracy": round(latest_accuracy, 2),
            "drop": round(drop, 2)
        }