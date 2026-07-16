

class Regression_Detector:
    def detect(self,baseline_accuracy,candidate_accuracy,regression_threshold):

        drop=baseline_accuracy-candidate_accuracy

        if drop > regression_threshold:
            return {
                "status":"Fail",
                "drop": drop
            }
        return {
            "status":"Pass",
            "drop":drop
        }
