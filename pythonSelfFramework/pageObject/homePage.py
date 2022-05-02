from selenium.webdriver.common.by import By

class homePage:
    def __init__(self, driver):
        self.driver = driver

    itemss = (By.CSS_SELECTOR, "input.search-keyword")

    def cartItems(self):
        return self.driver.find_element(*homePage.itemss)
