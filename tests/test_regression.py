from src.regression import Regression_Detector


def test_regression_pass():
    detector = Regression_Detector()

    baseline = {
        "accuracy": 90,
        "results": [
            {"passed": True},
            {"passed": True},
            {"passed": False}
        ]
    }

    candidate = {
        "accuracy": 88,
        "results": [
            {"passed": True},
            {"passed": True},
            {"passed": False}
        ]
    }

    result = detector.detect(baseline, candidate, 3)

    assert result["status"] == "PASS"
    assert result["drop"] == 2
    assert result["regressions"] == 0
    assert result["improvements"] == 0


def test_regression_fail():
    detector = Regression_Detector()

    baseline = {
        "accuracy": 90,
        "results": [
            {"passed": True},
            {"passed": True},
            {"passed": True}
        ]
    }

    candidate = {
        "accuracy": 80,
        "results": [
            {"passed": False},
            {"passed": True},
            {"passed": False}
        ]
    }

    result = detector.detect(baseline, candidate, 3)

    assert result["status"] == "FAIL"
    assert result["drop"] == 10
    assert result["regressions"] == 2
    assert result["improvements"] == 0