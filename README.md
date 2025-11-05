# QA Web Automation (Selenium + pytest)

Runs UI tests against a local login page at `http://127.0.0.1:5500/index.html`.

## Setup
```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -U pip -r requirements.txt

## Summary
This project automates login validation for a custom HTML/CSS/JS website using Selenium and pytest. 
It includes tests for valid and invalid credentials, HTML reporting, and uses the Page Object Model structure.

## Tools Used
- Python
- Selenium
- pytest
- pytest-html
- webdriver-manager