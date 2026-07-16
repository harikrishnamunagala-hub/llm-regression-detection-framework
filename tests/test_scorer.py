from src.scorer import Scorer

def test_exact_match():
    scorer = Scorer()
    assert scorer.score("Tokyo", "Tokyo") == 1

def test_wrong_answer():
    scorer = Scorer()
    assert scorer.score("Tokyo", "Delhi") == 0