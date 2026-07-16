from src.models import MockModel,GeminiModel

class ModelFactory:

    @staticmethod
    def create_model(provider,role,model_name=None):

        if provider == "mock":
            return MockModel(role)

        elif provider == "gemini":
            return GeminiModel(model_name)

        else:
            raise ValueError(f"Unknown model: {model_name}")