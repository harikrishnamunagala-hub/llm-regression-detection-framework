from .exact_match import ExactMatchScorer
from .rapidfuzz_scorer import RapidFuzzScorer
from .semantic_scorer import SemanticSimilarityScorer


class ScorerFactory:

    @staticmethod
    def create_scorer(scorer_name):

        if scorer_name == "exact_match":
            return ExactMatchScorer()
        
        elif scorer_name== "rapidfuzz_scorer":
            return RapidFuzzScorer()
        
        elif scorer_name=="semantic_scorer":
            return SemanticSimilarityScorer()
            

        raise ValueError(f"Unknown scorer: {scorer_name}")