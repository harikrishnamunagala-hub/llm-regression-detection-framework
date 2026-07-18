from rapidfuzz import fuzz
from .base_scorer import BaseScorer


class RapidFuzzScorer(BaseScorer):

    def __init__(self, threshold=90):
        self.threshold = threshold

    def score(self, expected, generated):

        expected = expected.lower().strip()
        generated = generated.lower().strip()

        similarity = fuzz.token_set_ratio(expected, generated)

        return {
            "passed": similarity >= self.threshold,
            "metric": "RapidFuzz Token Set",
            "metric_score": round(similarity, 2),
            "threshold": self.threshold
        }