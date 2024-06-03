from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageObjects.base import BasePage
from selenium.webdriver.common.by import By
from conf import *


class MainPage(BasePage):
    INPUT_SEARCH = (By.CSS_SELECTOR, "div.container div.row div.col-sm-5 div.input-group > input.form-control.input-lg")
    BUTTON_CART_TOTAL = (By.CSS_SELECTOR, "#cart-total")
    BUTTON_CART = (By.XPATH, "//body/nav[@id='top']/div[1]/div[1]/ul[1]/li[4]/a[1]")
    BUTTON_REGLOG = (
        By.CSS_SELECTOR, "div.container div.nav.pull-right ul.list-inline li.dropdown:nth-child(2) > a.dropdown-toggle"
    )

    BUTTON_REGISTER = (By.LINK_TEXT, "Регистрация")
    BUTTON_LOGIN = (By.LINK_TEXT, "Авторизация")
    BUTTON_HOME = (By.LINK_TEXT, "Интернет магазин Opencart")

    DROPDOWN_TABLET = (By.LINK_TEXT, "Планшеты")
    PRODUCT_TABLET = (By.LINK_TEXT, "Samsung Galaxy Tab 10.1")

    DROPDOWN_TELEPHONE_HTC = (By.LINK_TEXT, "Телефоны")
    PRODUCT_TELEPHONE_HTC = (By.LINK_TEXT, "HTC Touch HD")

    DROPDOWN_PC = (By.LINK_TEXT, "Компьютеры")
    LI_PC = (By.LINK_TEXT, "PC (0)")

    PRODUCTS = [
        (By.CSS_SELECTOR, product.format(str(i), element))
        for i in range(1, 5)
    ]

    PRODUCTS_BUTTON_BUY = [
        (By.CSS_SELECTOR, product.format(str(i), button_buy))
        for i in range(1, 5)
    ]

    PRODUCTS_BUTTON_FAVORITE = [
        (By.CSS_SELECTOR, product.format(str(i), button_fav))
        for i in range(1, 5)
    ]

    LAST_INDEX = len(PRODUCTS) - 1

    def open_category(self, category_name):
        category_link = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"//a[contains(text(),'{category_name}')]"))
        )
        category_link.click()

    def open_category_camera(self):
        category_link = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Canon EOS 5D')]]"))
        )
        category_link.click()

    def search(self, search_query):
        search_input = self.find_element((By.CSS_SELECTOR, "div.input-group > input.form-control.input-lg"))
        search_input.send_keys(search_query)
        search_button = self.find_element((By.CSS_SELECTOR, "div.input-group span.input-group-btn > button.btn.btn-default.btn-lg"))
        search_button.click()

    PC_CATEGORY_LINK = (By.CSS_SELECTOR,
                        "div.container:nth-child(3) nav.navbar div.collapse.navbar-collapse.navbar-ex1-collapse ul.nav.navbar-nav li.dropdown:nth-child(1) > a.dropdown-toggle")
    PC_CATEGORY_ITEM = (By.CSS_SELECTOR,
                        "div.container:nth-child(3) nav.navbar div.collapse.navbar-collapse.navbar-ex1-collapse ul.nav.navbar-nav li.dropdown:nth-child(1) div.dropdown-menu div.dropdown-inner ul.list-unstyled li:nth-child(1) > a:nth-child(1)")
    PRODUCT_ITEMS = (By.CSS_SELECTOR,
                     "div.container:nth-child(3) nav.navbar div.collapse.navbar-collapse.navbar-ex1-collapse ul.nav.navbar-nav li.dropdown:nth-child(1) div.dropdown-menu div.dropdown-inner ul.list-unstyled li:nth-child(1) > a:nth-child(1)")

    def open_pc_category(self):
        pc_category_link = self.find_element(self.PC_CATEGORY_LINK)
        pc_category_link.click()
        pc_category_item = self.find_element(self.PC_CATEGORY_ITEM)
        pc_category_item.click()

    def get_product_items(self):
        return self.find_elements(self.PRODUCT_ITEMS)
