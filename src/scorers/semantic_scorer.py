from sentence_transformers import SentenceTransformer, util
from .base_scorer import BaseScorer


class SemanticSimilarityScorer(BaseScorer):

    def __init__(self, threshold=0.70):
        self.threshold = threshold

        # Load model only once
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

        # Cache embeddings
        self.embedding_cache = {}

    def _normalize(self, text):
        return text.strip().lower()

    def _get_embedding(self, text):

        text = self._normalize(text)

        if text not in self.embedding_cache:
            self.embedding_cache[text] = self.model.encode(
                text,
                convert_to_tensor=True
            )

        return self.embedding_cache[text]

    def score(self, expected, generated):

        expected_embedding = self._get_embedding(expected)
        generated_embedding = self._get_embedding(generated)

        similarity = util.cos_sim(
            expected_embedding,
            generated_embedding
        ).item()

        # Uncomment while debugging
        # print(f"Expected: {expected}")
        # print(f"Generated: {generated}")
        # print(f"Similarity: {similarity:.4f}\n")

        return {
            "passed": similarity >= self.threshold,
            "metric": "Semantic Similarity",
            "metric_score": round(similarity, 4),
            "threshold": self.threshold
        }