import time

import allure

from PageObjects.cart import CartPage
from PageObjects.home import MainPage
from PageObjects.product import ProductPage
from PageObjects.registration import RegistrationPage


@allure.feature("1st test")
@allure.title("Screenshot")
def test_screen(driver, logger):
    home = MainPage(driver, logger)
    home.open_website()
    product_page = ProductPage(driver, logger)
    product_page.open_product()
    product_page.open_thumbnail()
    product_page.next_lightbox()
    time.sleep(10)


@allure.feature("2nd test")
@allure.title("add to cart")
def test_korzina(driver, logger):
    home = MainPage(driver, logger)
    home.open_website()
    cart_page = CartPage(driver, logger)
    cart_page.add_to_cart()
    cart_page.open_cart()
    cart_items = cart_page.get_cart_items()
    if cart_items:
        print("Корзина не пуста")
    else:
        print("Корзина пуста")


@allure.feature("3rd test")
@allure.title("computer category")
def test_pc(driver, logger):
    home = MainPage(driver, logger)
    home.open_website()
    home.open_pc_category()
    product_items = home.get_product_items()
    if product_items:
        print("Страница категории PC пуста.")
    else:
        print("Страница категории PC не пуста.")


@allure.feature("4th test")
@allure.title("Registration")
def test_reg(driver, logger):
    home = MainPage(driver, logger)
    home.open_website()
    register_page = RegistrationPage(driver, logger)
    register_page.open_register_page()
    register_page.registration()


@allure.feature("5th test")
@allure.title("Search")
def test_search(driver, logger):
    home = MainPage(driver, logger)
    home.open_website()
    home.search("камера")


@allure.feature("6th test")
@allure.title("Wishlist")
def test_fav(driver, logger):
    home = MainPage(driver, logger)
    home.open_website()
    product_page = ProductPage(driver, logger)
    product_page.add_to_wishlist(2)


@allure.feature("7th test")
@allure.title("Camera")
def test_cam(driver, logger):
    home = MainPage(driver, logger)
    home.open_website()
    product_page = ProductPage(driver, logger)
    product_page.add_to_cart(4)
    product_page.camera()


@allure.feature("8th test")
@allure.title("Tablet")
def test_tab(driver, logger):
    home = MainPage(driver, logger)
    home.open_website()
    home.open_category("Планшеты")
    product_page = ProductPage(driver, logger)
    product_page.add_to_cart_tablet()


@allure.feature("9th test")
@allure.title("HTC")
def test_htc(driver, logger):
    home = MainPage(driver, logger)
    home.open_website()
    home.open_category("Телефоны")
    product_page = ProductPage(driver, logger)
    product_page.add_to_cart_htc()


@allure.feature("10th test")
@allure.title("Review")
def test_rev(driver, logger):
    home = MainPage(driver, logger)
    home.open_website()
    home.open_category("Apple Cinema 30")
    product_page = ProductPage(driver, logger)
    product_page.open_review_form()
    product_page.submit_review("UwU", "UwUWUWUUWUWUUWUWUUWUWUUWUWUUWUWUWUWUUWUWU")
