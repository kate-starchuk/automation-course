from typing import Tuple
from selenium.webdriver.common.by import By
from homework_16_framework.pages.product import Product

from homework_16_framework.pages.base_page import BasePage


class ProductList(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.__first_entry_locator: Tuple[By.XPATH, str] = (By.XPATH, '//div[@class="product-listing view-category"]/div[1]')

    def choose_product(self):
        self.click(self.__first_entry_locator)
        return Product(self.driver)
