from .base_model import BaseModel


class MockModel(BaseModel):

    def __init__(self, version):
        self.version = version

    def generate(self, question):

        baseline = {
            "What is 25 × 4?": "100",
            "What is the capital of Japan?": "Tokyo",
            "What data structure follows the Last In First Out (LIFO) principle?": "Queue",
            "What is the chemical symbol for gold?": "Au",
            "Who was the first President of the United States?": "George Washington"
        }

        candidate = {
            "What is 25 × 4?": "100",
            "What is the capital of Japan?": "Tokyo",
            "What data structure follows the Last In First Out (LIFO) principle?": "Queue",
            "What is the chemical symbol for gold?": "Gold",
            "Who was the first President of the United States?": "George Washington"
        }

        if self.version == "baseline":
            return baseline.get(question, "unknown")

        return candidate.get(question, "unknown")