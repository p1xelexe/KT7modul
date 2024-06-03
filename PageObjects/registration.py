import time

from PageObjects.base import BasePage
from selenium.webdriver.common.by import By
from conf import *


class RegistrationPage(BasePage):
    INPUT_FIRSTNAME = (By.CSS_SELECTOR, "#input-firstname")
    INPUT_LASTNAME = (By.CSS_SELECTOR, "#input-lastname")
    INPUT_EMAIL = (By.CSS_SELECTOR, "#input-email")
    INPUT_TELEPHONE = (By.CSS_SELECTOR, "#input-telephone")
    INPUT_PASSWORD = (By.CSS_SELECTOR, "#input-password")
    INPUT_CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#input-confirm")
    REGISTER_LINK = (By.CSS_SELECTOR,
                     "div.container div.nav.pull-right ul.list-inline li.dropdown.open:nth-child(2) ul.dropdown-menu.dropdown-menu-right li:nth-child(1) > a:nth-child(1)")
    MY_ACCOUNT_DROPDOWN = (
        By.CSS_SELECTOR, "div.container div.nav.pull-right ul.list-inline li.dropdown:nth-child(2) > a.dropdown-toggle")
    BUTTON_ACCEPTANCE = (By.XPATH, "//body/div[@id='account-register']/div[1]/div[1]/form[1]/div[1]/div[1]/input[1]")
    BUTTON_NEXT = (By.XPATH, "//body/div[@id='account-register']/div[1]/div[1]/form[1]/div[1]/div[1]/input[2]")

    BUTTON_TRUE_SUBNEWS = (
        By.XPATH,
        "//body/div[@id='account-register']/div[1]/div[1]/form[1]/fieldset[3]/div[1]/div[1]/label[1]/input[1]"
    )
    BUTTON_FALSE_SUBNEWS = (
        By.XPATH,
        "//body/div[@id='account-register']/div[1]/div[1]/form[1]/fieldset[3]/div[1]/div[1]/label[2]/input[1]"
    )

    inputs = [
        INPUT_FIRSTNAME, INPUT_LASTNAME, INPUT_EMAIL, INPUT_TELEPHONE, INPUT_PASSWORD, INPUT_CONFIRM_PASSWORD
    ]

    def registration(self):
        for input_field, input_text in zip(self.inputs, input_texts):
            self.Pinput(input_field, input_text)

    def Pinput(self, input_field, input_text):
        self.click(input_field)
        self.write(input_field, input_text)
        time.sleep(2)

    def login(self):
        for input_field, input_text in zip([self.INPUT_EMAIL, self.INPUT_PASSWORD], [email, passw, conpassw]):
            self.Pinput(input_field, input_text)

    # def Pinput(self, input_field, input_text):
    #     self.click(input_field)
    #     self.write(input_field, input_text)
    #     time.sleep(2)

    def open_register_page(self):
        my_account_dropdown = self.find_element(self.MY_ACCOUNT_DROPDOWN)
        my_account_dropdown.click()
        register_link = self.find_element(self.REGISTER_LINK)
        register_link.click()

    def click(self, input_field):
        self.find_element(input_field).click()
        pass

    def write(self, input_field, input_text):
        self.find_element(input_field).send_keys(input_text)
        pass
