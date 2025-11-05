from selenium.webdriver.common.by import By


class LoginPage:

    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    SUBMIT = (By.ID, "submit")
    ERROR = (By.ID, "error")


    def __init__(self, driver):
        self.driver = driver
    
    def open(self, url):
        self.driver.get(url)
    
    def login(self, username, password):
        self.driver.find_element(*self.USERNAME).clear()
        self.driver.find_element(*self.USERNAME).send_keys(username)
        self.driver.find_element(*self.PASSWORD).clear()
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        self.driver.find_element(*self.SUBMIT).click()

    def error_text(self):
        return self.driver.find_element(*self.ERROR).text        
