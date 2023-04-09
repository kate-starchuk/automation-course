from typing import Tuple

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from homework_16_framework.pages.base_page import BasePage
from homework_16_framework.pages.product_list import ProductList


class Dashboard(BasePage):

    def __init__(self, driver: Chrome):
        super().__init__(driver)

    def choose_category(self):
        category_locator: Tuple[By.XPATH, str] = (By.XPATH, f'//div[@class="home-navigation"]/button[6]')
        self.click(category_locator)
        return ProductList(self.driver)

