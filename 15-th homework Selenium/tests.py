from time import sleep

from selenium.webdriver import Chrome, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


def test_1():
    driver = Chrome("drivers/chromedriver")
    driver.get("https://www.yakaboo.ua/ua/knigi.html")
    search_input_locator = '//input[@id="search"]'
    first_list_item_locator = '//div[@class="ui-search-result__products"]//div[@class="ui-search-product"]/a'
    search_input: WebElement = driver.find_element(By.XPATH, search_input_locator)
    search_input.send_keys("Чорна рада, Пантелеймон Куліш")
    sleep(1)
    first_list_item: WebElement = driver.find_element(By.XPATH, first_list_item_locator)
    first_list_item.click()
    sleep(2)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    sleep(3)
    driver.quit()
