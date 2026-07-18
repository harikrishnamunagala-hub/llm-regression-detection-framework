from src.regression import Regression_Detector

def test_regression_pass():
    detector = Regression_Detector()

    baseline = {"accuracy": 90}
    candidate = {"accuracy": 88}

    result = detector.detect(baseline, candidate, 3)

    assert result["status"] == "PASS"


def test_regression_fail():
    detector = Regression_Detector()

    baseline = {"accuracy": 90}
    candidate = {"accuracy": 80}

    result = detector.detect(baseline, candidate, 3)

    assert result["status"] == "FAIL"