import os
from dotenv import load_dotenv

load_dotenv()

class SlackNotifier:
    def __init__(self):
        self.webhook_url = os.getenv("SLACK_WEBHOOK_URL")

    def send(self, message):
        if not self.webhook_url:
            print("Slack webhook not configured. Skipping notification.")
            return

        # existing Slack sending code