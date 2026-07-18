import yaml


class PromptLoader:

    @staticmethod
    def load_prompt(path):

        with open(path, "r", encoding="utf-8") as file:
            return yaml.safe_load(file)