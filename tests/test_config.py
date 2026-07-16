from src.config import ConfigLoader

def test_config_load():
    config = ConfigLoader.load_config("config/config.yaml")
    assert "baseline" in config
    assert "candidate" in config