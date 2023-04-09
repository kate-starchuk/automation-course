from selenium.webdriver.common.by import By
from homework_16_framework.pages.base_page import BasePage


class Product(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def get_title(self):
        el = self.wait_for_element((By.XPATH, f"//h1"))
        return el.get_attribute("innerText").strip()

    def wait_for_modal(self):
        product_modal_locator = (By.XPATH, "//div[@class='product-overlay']")
        self.wait_for_element(product_modal_locator)
