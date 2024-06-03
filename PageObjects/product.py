from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.base import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

from conf import *
import time


class ProductPage(BasePage):
    MAIN_PICTURE = (By.XPATH, "//body/div[@id='product-product']/div[1]/div[1]/div[1]/div[1]/ul[1]/li[1]/a[1]")
    BUTTON_HOME = (By.LINK_TEXT, "Интернет магазин Opencart")
    BUTTON_FAVORITE = (By.XPATH, "//body/div[@id='product-product']/div[1]/div[1]/div[1]/div[2]/div[1]/button[1]")
    BUTTON_BUY = (By.CSS_SELECTOR, "#button-cart")
    BUTTON_NEXT_REVIEW = (By.CSS_SELECTOR, "#button-review")
    INPUT_COUNT = (By.CSS_SELECTOR, "#input-quantity")
    BUTTON_DESCRIPTION = (By.LINK_TEXT, "Описание")
    BUTTON_CHARACTERISTICS = (By.LINK_TEXT, "Характеристики")
    BUTTON_REVIEW = (By.PARTIAL_LINK_TEXT, "Отзывов (")
    INPUT_NAME_REVIEW = (By.CSS_SELECTOR, "#input-name")
    INPUT_REVIEW = (By.CSS_SELECTOR, "#input-review")
    SELECT_COLOR = (By.CSS_SELECTOR, "#input-option226")
    SELECT_OPTION_COLOR = (By.XPATH, "//option[contains(text(),'Blue')]")
    PRODUCT_NAME = (By.CSS_SELECTOR,
                    "div.container:nth-child(4) div.row div.col-sm-12 div.row:nth-child(4) div.product-layout.col-lg-3.col-md-3.col-sm-6.col-xs-12:nth-child(4) div.product-thumb.transition div.caption h4:nth-child(1) > a:nth-child(1)")
    THUMBNAILS = (By.CSS_SELECTOR,
                  "div.container:nth-child(4) div.row div.col-sm-12 div.row div.col-sm-8 ul.thumbnails li > a.thumbnail")
    LIGHTBOX_NEXT = (By.CSS_SELECTOR,
                     "body:nth-child(2) div.mfp-wrap.mfp-gallery.mfp-close-btn-in.mfp-auto-cursor.mfp-ready:nth-child(2) div.mfp-container.mfp-s-ready.mfp-image-holder > button.mfp-arrow.mfp-arrow-right.mfp-prevent-close:nth-child(4)")

    BUTTON_REVIEW_MARK = [2, 3, 4, 5, 6]
    BUTTON_REVIEW_MARK = [
        (By.CSS_SELECTOR, review_cs.format(mark))
        for mark in BUTTON_REVIEW_MARK
    ]

    def kaka(self, count: int):
        action_chains = ActionChains(self.driver)

        for _ in range(count):
            action_chains.key_down(Keys.CONTROL).send_keys(Keys.ARROW_RIGHT).key_up(Keys.CONTROL).perform()
            time.sleep(1)

        time.sleep(1)

    def open_product(self):
        product_name = self.find_element(self.PRODUCT_NAME)
        product_name.click()

    def open_thumbnail(self):
        thumbnail = self.find_elements(self.THUMBNAILS)[0]
        thumbnail.click()

    def next_lightbox(self):
        next_button = self.find_element(self.LIGHTBOX_NEXT)
        next_button.click()

    def add_to_cart(self, product_number):
        add_to_cart_button = self.find_element((By.CSS_SELECTOR,
                                                f"div.container:nth-child(4) div.row div.col-sm-12 div.row:nth-child("
                                                f"4) "
                                                f"div.product-layout.col-lg-3.col-md-3.col-sm-6.col-xs-12:nth-child("
                                                f"{product_number}) div.product-thumb.transition div.button-group > "
                                                f"button:nth-child(1)"))
        add_to_cart_button.click()

    def add_to_cart_tablet(self):
        add_to_cart_button = self.find_element((By.XPATH,
                                                "//body/div[@id='product-category']/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/button[1]/i[1]"))
        add_to_cart_button.click()

    def add_to_cart_htc(self):
        add_to_cart_button = self.find_element(
            (By.XPATH, "//body/div[@id='product-category']/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/button[1]"))
        add_to_cart_button.click()

    def add_to_cart_camera(self):
        add_to_cart_button = self.find_element(
            (By.XPATH, "//body/main[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/form[1]/div[1]/button[1]/i[1]"))
        add_to_cart_button.click()

    def add_to_wishlist(self, product_number):
        add_to_wishlist_button = self.find_element((By.CSS_SELECTOR,
                                                    f"div.container:nth-child(4) div.row div.col-sm-12 div.row:nth-child(4) div.product-layout.col-lg-3.col-md-3.col-sm-6.col-xs-12:nth-child({product_number}) div.product-thumb.transition div.button-group button:nth-child(2) > i.fa.fa-heart"))
        add_to_wishlist_button.click()

    def open_product_images(self, product_number):
        product_link = self.find_element((By.CSS_SELECTOR,
                                          f"div.container:nth-child(4) div.row div.col-sm-12 div.row:nth-child(4) div.product-layout.col-lg-3.col-md-3.col-sm-6.col-xs-12:nth-child({product_number}) div.product-thumb.transition div.caption h4:nth-child(1) > a:nth-child(1)"))
        product_link.click()
        product_image = self.find_element((By.CSS_SELECTOR, "div.col-sm-8 ul.thumbnails li:nth-child(1) > a.thumbnail"))
        product_image.click()

    def switch_product_images(self):
        next_image_button = self.find_element((By.CSS_SELECTOR,
                                               "body:nth-child(2) div.mfp-wrap.mfp-gallery.mfp-close-btn-in.mfp-auto-cursor.mfp-ready:nth-child(2) div.mfp-container.mfp-s-ready.mfp-image-holder > button.mfp-arrow.mfp-arrow-right.mfp-prevent-close:nth-child(4)"))
        next_image_button.click()

    def open_review_form(self):
        review_link = self.find_element((By.XPATH, "//a[contains(text(),'Отзывов (0)')]"))
        review_link.click()

    def submit_review(self, name, review_text):
        name_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'input-name')))
        name_input.send_keys(name)
        self.driver.implicitly_wait(3)

        review_input = self.find_element((By.ID, 'input-review'))
        review_input.send_keys(review_text)
        self.driver.implicitly_wait(3)

        rating_input = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH,
                                        "//body/div[@id='product-product']/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/form[1]/div[4]/div[1]/input[3]")))

        actions = ActionChains(self.driver)
        actions.move_to_element(rating_input).click().perform()

        self.driver.execute_script("arguments[0].scrollIntoView(true);", rating_input)
        self.driver.implicitly_wait(3)

        rating_input.click()
        self.driver.implicitly_wait(3)

        submit_button = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.ID, "button-review")))
        self.driver.execute_script("arguments[0].click();", submit_button)

        self.driver.implicitly_wait(3)

    def camera(self):
        camera_option = self.find_element((By.ID, "input-option226"))
        camera_option.click()
        camera_option.send_keys(Keys.ARROW_DOWN)
        add_to_cart_button = self.find_element((By.ID, "button-cart"))
        add_to_cart_button.click()
