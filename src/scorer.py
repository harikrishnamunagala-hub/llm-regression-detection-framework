class Scorer:
    def score(self,expected_answer,generated_answer):

        expected=expected_answer.lower().strip()
        generated=generated_answer.lower().strip()
        if expected in generated:
            return 1
        return 0