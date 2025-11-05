from selenium.webdriver.common.by import By

class SecurePage:

    HEADING = (By.TAG_NAME, "h1")
    LOGOUT = (By.XPATH, "//a[contains(@href, 'logout')]")
    
    def __init__(self, driver):
        self.driver = driver

    def heading_text(self):
        return self.driver.find_element(*self.HEADING).text

    def logout_visible(self):
        return len(self.driver.find_elements(*self.LOGOUT)) > 0
