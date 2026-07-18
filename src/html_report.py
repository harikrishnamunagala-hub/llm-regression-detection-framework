from jinja2 import Environment, FileSystemLoader
from src.history import HistoryManager


class HTMLReportGenerator:

    def __init__(self):

        self.env = Environment(
            loader=FileSystemLoader("templates")
        )

        self.template = self.env.get_template("report.html")

        self.history_manager = HistoryManager()

    def generate(
        self,
        baseline,
        candidate,
        regression,
        config
    ):

        history = self.history_manager.load_history()

        html = self.template.render(

            baseline=baseline,

            candidate=candidate,

            regression=regression,

            config=config,

            history=history

        )

        with open(
            "reports/report.html",
            "w",
            encoding="utf-8"
        ) as file:

            file.write(html)