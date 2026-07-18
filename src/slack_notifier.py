import os
import requests
from dotenv import load_dotenv

load_dotenv()


class SlackNotifier:
    def __init__(self):
        self.webhook_url = os.getenv("SLACK_WEBHOOK_URL")

        if not self.webhook_url:
            raise ValueError("SLACK_WEBHOOK_URL not found in .env")

    def send(self,baseline_evaluation,candidate_evaluation, regression_report):
        message = {
            "text": (
                "🤖 *LLM Regression Detection Report*\n\n"
                f"*Status:* {regression_report['status']}\n"
                f"*Baseline Accuracy:* {baseline_evaluation['accuracy']:.2f}%\n"
                f"*Candidate Accuracy:* {candidate_evaluation['accuracy']:.2f}%\n"
                f"*Accuracy Drop:* {regression_report['drop']:.2f}%\n"
                
                f"*Regressions:* {regression_report['regressions']}\n"
                f"*Improvements:* {regression_report['improvements']}"
            )
        }

        response = requests.post(self.webhook_url, json=message)

        if response.status_code == 200:
            print("✅ Slack notification sent successfully.")
        else:
            print(f"❌ Slack notification failed: {response.status_code}")
            print(response.text)