import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage

from .base_model import BaseModel

load_dotenv()


class GeminiModel(BaseModel):

    def __init__(self, model_name):

        self.model = ChatGoogleGenerativeAI(
            model=model_name,
            google_api_key=os.getenv("GOOGLE_API_KEY"),
            temperature=0
        )

    def generate(self, question, prompt):

        messages = [
            SystemMessage(content=prompt["system_prompt"]),
            HumanMessage(content=question)
        ]

        response = self.model.invoke(messages)

        return response.text