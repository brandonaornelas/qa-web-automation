# 🧪 QA Web Automation — Login Page Testing

This project contains an automated test suite built with **Python**, **Selenium**, and **pytest** to verify the functionality of a custom login web page.  
It is connected to my front-end project [**log-test-page**](https://github.com/brandonaornelas/log-test-page), which was designed specifically to be tested with this framework.

---

## 🧠 Project Overview

The purpose of this project is to demonstrate **end-to-end QA automation** on a simple login page built with **HTML, CSS, and JavaScript**.  
The automation validates both **successful** and **unsuccessful** login attempts, ensuring correct error handling and UI behavior.

The website tested (log-test-page) runs locally on **Live Server (port 5500)**.

---

## ⚙️ Tech Stack

| Tool | Purpose |
|------|----------|
| **Python 3** | Main programming language |
| **Selenium WebDriver** | Automates browser interactions |
| **pytest** | Test framework for organizing and running tests |
| **pytest-html** | Generates readable HTML test reports |
| **webdriver-manager** | Handles ChromeDriver automatically |
| **VS Code / GitHub** | Development and version control |

---

## 🧩 Folder Structure

```
qa-web-automation/
├── pages/
│   ├── login_page.py       # Page Object for login interactions
│   └── secure_page.py      # Page Object for post-login validation
├── tests/
│   └── test_login.py       # Test cases for valid/invalid logins
├── conftest.py             # Driver setup and base URL
├── requirements.txt        # Dependencies
├── pytest.ini
├── README.md
└── reports/                # HTML test reports (after running)
```

---

## 🧰 Setup & Installation

### 1. Clone both repos
```bash
git clone https://github.com/brandonaornelas/log-test-page.git
git clone https://github.com/brandonaornelas/qa-web-automation.git
```

### 2. Run the login page
Open the `log-test-page` folder in VS Code  
and start the **Live Server** extension.  
It should open automatically at:
```
http://127.0.0.1:5500/index.html
```

### 3. Set up the automation environment
In the `qa-web-automation` folder:
```bash
python3 -m venv .venv
source .venv/bin/activate   # (Mac/Linux)
# OR
.venv\Scripts\activate      # (Windows)

pip install -r requirements.txt
```

---

## ▶️ Running the Tests

Run all tests:
```bash
pytest -v
```

Generate a test report:
```bash
pytest -v --html=reports/report.html --self-contained-html
```

Open the HTML report in your browser:
```
qa-web-automation/reports/report.html
```

---

## ✅ What’s Being Tested

1. **Valid login** → Correct credentials redirect to the secure page  
   - Expected message: `Logged In Successfully`
2. **Invalid username** → Shows: `Your username is invalid!`
3. **Invalid password** → Shows: `Your password is invalid!`
4. **Empty fields** → Shows proper validation messages

Each case is run automatically in a headless Chrome browser.

---

## 🧱 Page Object Model (POM)

This project follows the **Page Object Model** design pattern:
- Keeps selectors and actions in separate files
- Makes test cases clean, readable, and scalable

Example:
```python
lp = LoginPage(driver)
lp.open(base_url)
lp.login("student", "Password123")
```

---

## 📊 Example Output

All tests passed successfully ✅  
Generated HTML report (`reports/report.html`):

![Test Report Screenshot](reports/report_screenshot.png)

---

## 💬 What I Learned

- How to build and structure an automation framework using Selenium and pytest  
- How to create and reuse Page Object Models  
- How to validate UI elements and handle negative test cases  
- How to generate test reports and integrate them with version control  
- How QA automation saves time by replacing repetitive manual testing

---

## 🔗 Related Project

🧱 **Frontend Tested:** [log-test-page](https://github.com/brandonaornelas/log-test-page)

This repository contains the custom login page built with HTML, CSS, and JavaScript — designed specifically for this automation suite.

---

## 👤 Author

**Brandon Ornelas**  
B.B.A. in Information Technology — Texas Tech University  
Aspiring QA Automation Engineer & Software Support Specialist  

[GitHub Profile](https://github.com/brandonaornelas)

