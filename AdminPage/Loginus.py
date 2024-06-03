from PageObjects.base import BasePage
from AdminPage.Adminus import AdminPage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    INPUT_LOGIN = (By.CSS_SELECTOR, "#input-username")
    INPUT_PASSWORD = (By.CSS_SELECTOR, "#input-password")
    NEXT = (By.XPATH, "//body/div[@id='container']/div[@id='content']/div[1]/div[1]/div[1]/div[1]/div[2]/form[1]/div[3]/button[1]")

    def login(self):
        self.Pinput(LoginPage.INPUT_LOGIN, "user")
        self.Pinput(LoginPage.INPUT_PASSWORD, "bitnami")
        self.click(LoginPage.NEXT)
        self.logger.info("ADMIN: FINISH LOGGING")
        self.click(AdminPage.MENU_CATALOG)
        self.click(AdminPage.LI_PRODUCTS)
