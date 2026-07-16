from src.regression import Regression_Detector

def test_regression_pass():
    detector = Regression_Detector()
    result = detector.detect(90, 88, 3)
    assert result["status"] == "Pass"

def test_regression_fail():
    detector = Regression_Detector()
    result = detector.detect(90, 80, 3)
    assert result["status"] == "Fail"