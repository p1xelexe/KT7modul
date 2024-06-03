from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver, logger):
        self.driver = driver
        self.logger = logger
        self.class_name = self.__class__.__name__
        self.url = "https://demo-opencart.ru/"

    def find_element(self, locator, time=10):
        self.logger.info(f"Finding element by locator: {locator}")
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        self.logger.info(f"Finding elements by locator: {locator}")
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def open_website(self):
        return self.driver.get(self.url)
