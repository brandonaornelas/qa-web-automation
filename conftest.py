import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

BASE_URL = "http://127.0.0.1:5500/index.html"


@pytest.fixture

def driver():
    opts = Options()
    opts.add_argument("--headless=new")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    service = Service(ChromeDriverManager().install())
    d = webdriver.Chrome(service=service, options=opts)
    d.set_window_size(1280, 900)
    yield d 
    d.quit()


@pytest.fixture
def base_url():
    return BASE_URL
