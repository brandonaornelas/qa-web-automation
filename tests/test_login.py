import pytest
from pages.login_page import LoginPage
from pages.secure_page import SecurePage

VALID_USER = "student"
VALID_PASS = "Password123"

def test_valid_login(driver, base_url):
    lp = LoginPage(driver)
    lp.open(base_url)
    lp.login(VALID_USER, VALID_PASS)
    sp = SecurePage(driver)
    assert sp.heading_text() == "Logged In Successfully"
    assert sp.logout_visible()

@pytest.mark.parametrize("user,pwd,expected", [
    ("wronguser", "Password123", "Your username is invalid!"),
    ("student", "wrongpass", "Your password is invalid!"),
    ("", "Password123", "Your username is invalid!"),
    ("student", "", "Your password is invalid!"),
])
def test_invalid_login(driver, base_url, user, pwd, expected):
    lp = LoginPage(driver)
    lp.open(base_url)
    lp.login(user, pwd)
    assert expected in lp.error_text()
