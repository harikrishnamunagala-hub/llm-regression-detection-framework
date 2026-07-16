<p align="center">
  <img src="assets/banner.png" width="100%">
</p>

<h1 align="center">
🤖 LLM Regression Detection Framework
</h1>

<p align="center">

Evaluate • Compare • Detect Regressions • Generate Reports

</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![LangChain](https://img.shields.io/badge/LangChain-green)
![Gemini](https://img.shields.io/badge/Google-Gemini-orange)
![YAML](https://img.shields.io/badge/Configuration-YAML-blue)
![Markdown](https://img.shields.io/badge/Reports-Markdown-lightgrey)

</p>

---

> **A modular framework for evaluating Large Language Models (LLMs), comparing model versions, detecting regressions, measuring inference latency, and generating automated evaluation reports.**

## 🎯 Key Highlights

- 🔹 Provider-based LLM evaluation framework
- 🔹 Modular architecture with Factory Design Pattern
- 🔹 YAML-driven configuration (no hardcoded model selection)
- 🔹 Automated regression detection using configurable thresholds
- 🔹 Accuracy and latency benchmarking
- 🔹 Markdown report generation for evaluation analysis
- 🔹 Real Google Gemini API integration
- 🔹 Easily extensible to new providers, scorers, and benchmark datasets

## 📚 Table of Contents

- [Overview](#-overview)
- [Motivation](#-motivation)
- [Architecture](#-architecture)
- [Evaluation Workflow](#-evaluation-workflow)
- [Features](#-features)
- [Project Structure](#-project-structure)
- [How It Works](#-how-it-works)
- [Sample Console Output](#-sample-console-output)
- [Generated Report](#-generated-report)
- [Design Principles](#-design-principles)
- [Tech Stack](#-tech-stack)
- [Roadmap](#-roadmap)
- [Author](#-author)

## 📖 Overview

The **LLM Regression Detection Framework** is a modular evaluation pipeline designed to compare Large Language Models (LLMs), identify performance regressions, and generate structured evaluation reports.

As LLMs evolve through new model releases, fine-tuning, or prompt modifications, even small changes can unintentionally degrade performance on previously solved tasks. This framework automates the evaluation process by comparing a baseline model against a candidate model using a configurable golden dataset.

The framework measures response accuracy, tracks inference latency, detects regressions using configurable thresholds, and generates detailed Markdown reports for analysis. Its modular architecture enables easy integration of new model providers, evaluation metrics, scoring strategies, and benchmark datasets with minimal code changes.

By separating configuration, model abstraction, evaluation logic, and reporting, the framework demonstrates software engineering practices commonly used in production AI systems.


## 🎯 Motivation

Large Language Models are evolving rapidly through new model releases, prompt engineering, and fine-tuning. While these updates often improve overall performance, they can also introduce regressions where previously correct responses become incorrect.

Unlike traditional software, evaluating LLMs requires comparing generated responses rather than deterministic outputs. This project applies software engineering principles to LLM evaluation by providing an automated regression testing framework that measures accuracy, tracks latency, compares model versions, and generates structured evaluation reports.

The framework aims to simplify model validation before deployment and serves as a foundation for integrating advanced evaluation metrics and industry-standard benchmark datasets.


## 🏗 Architecture

<p align="center">
    <img src="assets/architecture.png" width="900">
</p>

## 🔄 Evaluation Workflow

```text
                   config.yaml
                         │
                         ▼
                  Load Configuration
                         │
                         ▼
                   Initialize Models
                (Baseline & Candidate)
                         │
                         ▼
                 Load Golden Dataset
                         │
                         ▼
                  Generate Responses
                         │
                         ▼
                  Compute Evaluation
          (Accuracy + Latency + Scores)
                         │
                         ▼
                Detect Performance
                    Regression
                         │
                         ▼
           Generate Markdown Report
```

## ✨ Features

- Provider-based model abstraction
- Factory Design Pattern for model initialization
- YAML-driven configuration
- Golden dataset evaluation
- Exact Match scoring
- Accuracy calculation
- Average latency measurement
- Threshold-based regression detection
- Automatic Markdown report generation
- Structured logging
- Google Gemini integration
- Mock model support for offline testing
- Extensible modular architecture

## 📂 Project Structure

```text
LLM_Regression_Detection/
│
├── assets/
│   ├── architecture.png
│   ├── banner.png
│   └── report_sample.png
│
├── config/
│   └── config.yaml
│
├── datasets/
│   ├── golden_dataset.json
│   └── test_dataset.json
│
├── reports/
│   └── evaluation_report.md
│
├── src/
│   ├── config.py
│   ├── datasets.py
│   ├── evaluator.py
│   ├── logger.py
│   ├── model_factory.py
│   ├── models.py
│   ├── regression.py
│   ├── report.py
│   └── scorer.py
│
├── tests/
│
├── app.py
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

### Folder Description

| Folder / File | Purpose |
|---------------|---------|
| `assets/` | README images, architecture diagram, report screenshots |
| `config/` | YAML configuration files |
| `datasets/` | Golden and test datasets used for evaluation |
| `reports/` | Automatically generated evaluation reports |
| `src/` | Core framework implementation |
| `tests/` | Unit tests |
| `app.py` | Entry point of the framework |
| `requirements.txt` | Python dependencies |
| `README.md` | Project documentation |

## 🧩 Core Components

| Component | Responsibility |
|------------|----------------|
| Config Loader | Loads framework configuration from YAML |
| Model Factory | Creates baseline and candidate model instances |
| Gemini Model | Connects to Google Gemini API |
| Mock Model | Offline testing without API calls |
| Evaluator | Runs model evaluation pipeline |
| Scorer | Computes Exact Match scores |
| Regression Detector | Detects performance degradation |
| Report Generator | Generates Markdown evaluation reports |
| Logger | Records framework execution logs |

## ⚙️ How It Works

The evaluation pipeline consists of the following stages:

1. Load framework configuration from `config.yaml`.

2. Initialize the baseline and candidate models using the Model Factory.

3. Load the evaluation dataset.

4. Generate responses for every question.

5. Compute Exact Match scores.

6. Measure inference latency for each response.

7. Calculate evaluation metrics including:
   - Accuracy
   - Correct Answers
   - Average Latency

8. Compare baseline and candidate performance.

9. Detect regression using the configured threshold.

10. Generate a detailed Markdown evaluation report.

## 📈 Sample Console Output

```text
============================================================
Baseline Accuracy      : 85.00%
Candidate Accuracy     : 85.00%

Baseline Avg Latency   : 3.5614 sec
Candidate Avg Latency  : 2.1762 sec

Accuracy Drop          : 0.00%
Status                 : PASS
============================================================
```

## 📄 Generated Evaluation Report

After every evaluation, the framework automatically generates a Markdown report containing:

- Evaluation summary
- Model information
- Accuracy comparison
- Latency comparison
- Regression status
- Failed test cases

<p align="center">
    <img src="assets/report_sample.png" width="900">
</p>

## 🏛 Design Principles

The framework follows several software engineering principles to ensure scalability and maintainability.

| Principle | Implementation |
|-----------|----------------|
| Separation of Concerns | Configuration, evaluation, scoring, reporting, and regression detection are implemented independently. |
| Factory Design Pattern | Dynamically creates different LLM providers without modifying evaluation logic. |
| Configuration over Hardcoding | YAML-based configuration allows switching models and datasets without code changes. |
| Extensibility | New providers, scorers, and benchmark datasets can be added with minimal modifications. |
| Reusability | Core evaluation components are independent and reusable across different workflows. |

## 💻 Tech Stack

| Category | Technology |
|-----------|------------|
| Programming Language | Python |
| LLM Framework | LangChain |
| Model Provider | Google Gemini |
| Configuration | YAML |
| Logging | Python Logging |
| Environment | python-dotenv |
| Report Format | Markdown |


# 📌 Project Highlights

This project demonstrates practical software engineering concepts applied to modern LLM systems.

### Engineering Concepts

- Modular Architecture
- Factory Design Pattern
- Configuration-Driven Development
- Automated Evaluation Pipeline
- Regression Testing
- Performance Monitoring
- Report Automation
- Extensible Component Design

### AI Concepts

- Large Language Model Evaluation
- Golden Dataset Testing
- Accuracy Benchmarking
- Latency Measurement
- Regression Detection
- Model Comparison


# 🚀 Roadmap

The project is actively being extended to support more advanced LLM evaluation capabilities.

## ✅ Version 1.0 (Current)

- [x] Modular project architecture
- [x] Provider-based Model Factory
- [x] Google Gemini integration
- [x] Mock model support
- [x] Golden Dataset evaluation
- [x] Exact Match scorer
- [x] Accuracy measurement
- [x] Latency measurement
- [x] Regression detection
- [x] Markdown report generation
- [x] YAML-driven configuration
- [x] Structured logging

---

## 🚧 Version 2.0 (Planned)

- [ ] RapidFuzz-based scoring
- [ ] Semantic similarity scoring
- [ ] Multiple evaluation metrics (Precision, Recall, F1)
- [ ] Benchmark dataset support (MMLU, GSM8K, HumanEval)
- [ ] FastAPI REST API
- [ ] Docker containerization
- [ ] GitHub Actions CI pipeline
- [ ] Unit testing suite
- [ ] Multi-provider support (OpenAI, Ollama, Anthropic)
- [ ] Interactive evaluation dashboard
- [ ] Result visualization using charts

# 👨‍💻 Author

**Hari Krishna**

### Areas of Interest

- Large Language Models (LLMs)
- Retrieval-Augmented Generation (RAG)
- Machine Learning
- AI Infrastructure
- MLOps

---

If you found this project interesting, feel free to connect or provide feedback.