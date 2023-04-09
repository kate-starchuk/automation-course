from selenium.webdriver.common.by import By


def test_get_product(dashboard):
    product_list = dashboard.choose_category()
    item_page = product_list.choose_product()
    item_page.wait_for_modal()
    title = 'Настільна гра Strateg Карти мемчики та котики (30729)'
    assert item_page.get_title() == title



