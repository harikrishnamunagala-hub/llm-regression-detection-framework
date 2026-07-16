from datetime import datetime


class Report_Generator:

    def generate_report(
        self,
        baseline_evaluation,
        candidate_evaluation,
        regression_report,
        config
    ):

        with open(config["report_path"], "w", encoding="utf-8") as file:

            # ===========================
            # Title
            # ===========================

            file.write("# Regression Evaluation Report\n\n")

            # ===========================
            # Evaluation Summary
            # ===========================

            file.write("## Evaluation Summary\n\n")

            file.write(
                f"**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
            )

            file.write(
                f"**Dataset:** {config['dataset_path']}\n\n"
            )

            file.write(
                f"**Total Questions:** {baseline_evaluation['total_questions']}\n\n"
            )

            # ===========================
            # Markdown Table
            # ===========================

            file.write("| Metric | Baseline | Candidate |\n")
            file.write("|--------|----------|-----------|\n")

            file.write(
                f"| Provider | {config['baseline']['provider']} | {config['candidate']['provider']} |\n"
            )

            file.write(
                f"| Model | {config['baseline']['model']} | {config['candidate']['model']} |\n"
            )

            file.write(
                f"| Accuracy | {baseline_evaluation['accuracy']:.2f}% | {candidate_evaluation['accuracy']:.2f}% |\n"
            )

            file.write(
                f"| Correct Answers | {baseline_evaluation['correct_answers']} | {candidate_evaluation['correct_answers']} |\n"
            )

            file.write(
                f"| Average Latency | {baseline_evaluation['average_latency']:.4f} sec | {candidate_evaluation['average_latency']:.4f} sec |\n"
            )

            file.write("\n")

            # ===========================
            # Regression Result
            # ===========================

            file.write("## Regression Result\n\n")

            file.write(
                f"- **Accuracy Drop:** {regression_report['drop']:.2f}%\n"
            )

            file.write(
                f"- **Status:** {regression_report['status']}\n\n"
            )

            # ===========================
            # Failed Baseline Cases
            # ===========================

            file.write("## Failed Test Cases\n\n")

            file.write("### Baseline Model\n\n")

            for result in baseline_evaluation["results"]:

                if result["score"] == 0:

                    file.write(f"#### Question {result['id']}\n\n")

                    file.write(
                        f"**Question**\n\n{result['question']}\n\n"
                    )

                    file.write(
                        f"**Expected Answer**\n\n{result['expected_answer']}\n\n"
                    )

                    file.write(
                        f"**Generated Answer**\n\n{result['generated_answer']}\n\n"
                    )

                    file.write(
                        f"**Latency:** {result['latency']:.4f} sec\n\n"
                    )

                    file.write("---\n\n")

            # ===========================
            # Failed Candidate Cases
            # ===========================

            file.write("### Candidate Model\n\n")

            for result in candidate_evaluation["results"]:

                if result["score"] == 0:

                    file.write(f"#### Question {result['id']}\n\n")

                    file.write(
                        f"**Question**\n\n{result['question']}\n\n"
                    )

                    file.write(
                        f"**Expected Answer**\n\n{result['expected_answer']}\n\n"
                    )

                    file.write(
                        f"**Generated Answer**\n\n{result['generated_answer']}\n\n"
                    )

                    file.write(
                        f"**Latency:** {result['latency']:.4f} sec\n\n"
                    )

                    file.write("---\n\n")