from PageObjects.base import BasePage
from selenium.webdriver.common.by import By


class CartPage(BasePage):
    ADD_TO_CART = (By.CSS_SELECTOR, "div.container:nth-child(4) div.row div.col-sm-12 div.row:nth-child(4) div.product-layout.col-lg-3.col-md-3.col-sm-6.col-xs-12:nth-child(2) div.product-thumb.transition div.button-group > button:nth-child(1)")
    CART_BUTTON = (By.CSS_SELECTOR, "div.container div.nav.pull-right ul.list-inline li:nth-child(4) a:nth-child(1) > i.fa.fa-shopping-cart")
    CART_ITEMS = (By.CSS_SELECTOR, ".table-bordered tr")
    SUCCESS_ALERT = (By.CSS_SELECTOR, ".alert-success")
    CART_CONTENT = (By.CSS_SELECTOR, "#content")

    def add_to_cart(self):
        add_button = self.find_element(self.ADD_TO_CART)
        add_button.click()

    def open_cart(self):
        cart_button = self.find_element(self.CART_BUTTON)
        cart_button.click()

    def get_cart_items(self):
        return self.find_elements(self.CART_ITEMS)
