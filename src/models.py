from abc import ABC, abstractmethod
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv

load_dotenv()

class BaseModel(ABC):
    @abstractmethod
    def generate(self,question):
        pass

class MockModel(BaseModel):
    def __init__(self,version):
        self.version=version

    def generate(self, question):
        baseline = {
            "What is 25 × 4?": "100",
            "What is the capital of Japan?": "Tokyo",
            "What data structure follows the Last In First Out (LIFO) principle?": "Queue",  # intentionally wrong
            "What is the chemical symbol for gold?": "Au",
            "Who was the first President of the United States?": "George Washington"
        }
        candidate = {
            "What is 25 × 4?": "100",
            "What is the capital of Japan?": "Tokyo",
            "What data structure follows the Last In First Out (LIFO) principle?": "Queue",   # Wrong
            "What is the chemical symbol for gold?": "Gold",                                  # Wrong
            "Who was the first President of the United States?": "George Washington"
        }
        if self.version=="baseline":
            return baseline.get(question,"unknown")


        return candidate.get(question,"unknown")
    

class GeminiModel(BaseModel):
    def __init__(self,model_name):
        self.model=ChatGoogleGenerativeAI(
            model=model_name,
            google_api_key=os.getenv("GOOGLE_API_KEY"),
            temperature=0
        )
    def generate(self,question):
        response=self.model.invoke([HumanMessage(content=question)])   
        return response.text

