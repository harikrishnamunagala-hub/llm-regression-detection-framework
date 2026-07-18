from src.models import MockModel,GeminiModel, OpenAIModel

class ModelFactory:

    @staticmethod
    def create_model(provider,role,model_name=None):

        if provider == "mock":
            return MockModel(role)

        elif provider == "gemini":
            return GeminiModel(model_name)

        elif provider == "openai":
            return OpenAIModel(model_name)

        else:
            raise ValueError(f"Unknown model: {provider}")