import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

from .base_model import BaseModel

load_dotenv()


class OpenAIModel(BaseModel):

    def __init__(self, model_name):

        self.model = ChatOpenAI(
            model=model_name,
            api_key=os.getenv("OPENAI_API_KEY"),
            temperature=0
        )

    def generate(self, question, prompt):

        messages = [
            SystemMessage(content=prompt["system_prompt"]),
            HumanMessage(content=question)
        ]

        response = self.model.invoke(messages)

        return response.content