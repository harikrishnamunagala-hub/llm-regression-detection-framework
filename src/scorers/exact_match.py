from .base_scorer import BaseScorer


class ExactMatchScorer(BaseScorer):

    def score(self, expected, generated):

        expected = expected.lower().strip()
        generated = generated.lower().strip()

        is_correct = expected in generated

        return {
        "passed": is_correct,
        "metric": "Exact Match",
        "metric_score": 100.0 if is_correct else 0.0,
        "threshold": 100
        }