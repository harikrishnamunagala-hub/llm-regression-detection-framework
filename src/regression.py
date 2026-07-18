

class Regression_Detector:
    def detect(self,baseline,candidate,threshold):

        baseline_accuracy = baseline["accuracy"]
        candidate_accuracy = candidate["accuracy"]

        drop = baseline_accuracy - candidate_accuracy

        if drop >= threshold:
            status = "FAIL"
        else:
            status = "PASS"

        regressions = 0
        improvements = 0

        for baseline_result, candidate_result in zip(
            baseline["results"],
            candidate["results"]
        ):

            if baseline_result["passed"] and not candidate_result["passed"]:
                regressions += 1

            elif (not baseline_result["passed"]) and candidate_result["passed"]:
                improvements += 1

        return {
            "drop": round(drop, 2),
            "status": status,
            "regressions": regressions,
            "improvements": improvements
        }
