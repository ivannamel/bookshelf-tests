<div align="center">
  <h1>📚 Bookshelf QA Automation Project</h1>
  <p>UI + API тесты для сайта <a href="https://demoqa.com/books">DemoQA Book Store</a>, написанные на Python с использованием Selenium, Pytest и Allure</p>
  <img src="https://img.shields.io/badge/Python-3.11-blue?logo=python">
  <img src="https://img.shields.io/badge/Selenium-Automation-green?logo=selenium">
  <img src="https://img.shields.io/badge/Pytest-Framework-blueviolet">
  <img src="https://img.shields.io/badge/API-Testing-orange">
</div>


# 📚 Bookshelf QA Automation Project

This project contains automated tests for the public demo site [DemoQA Book Store](https://demoqa.com/books).  
It includes both **UI** and **API** tests using modern best practices: Page Object Model, Pytest fixtures, and Allure reporting.

---

## 🛠 Tech Stack

- **Python 3**
- **Selenium** — UI automation
- **Requests** — API testing
- **Pytest** — test framework
- **Allure** — test reporting
- **Page Object Model (POM)** — scalable UI test structure

---

## 📁 Project Structure

<pre>
bookshelf-tests/
├── tests/
│   ├── api/                # API tests
│   └── ui/                 # UI tests
├── pages/                  # Page Object classes
├── utils/                  # Utilities (reserved for later)
├── conftest.py             # Pytest fixtures
├── requirements.txt
└── README.md
</pre>

---

🚀 Getting Started
1. Install dependencies
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

2. Run tests
UI tests:
pytest tests/ui/ --alluredir=allure-results
API tests:
pytest tests/api/ --alluredir=allure-results

3. Generate Allure report
allure serve allure-results

🎯 Example Tests

✅ API: Verify that a specific book (Git Pocket Guide) exists in the list.

🔍 UI: Search for a book title and validate that results contain the keyword.

🤝 Author: Ivanna
Feel free to fork, explore, and contribute!
