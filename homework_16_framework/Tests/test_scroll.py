from selenium.webdriver.common.by import By


def test_scroll_on_the_product(dashboard):
    product_list = dashboard.choose_category()
    item_page = product_list.choose_product()
    item_page.wait_for_modal()
    title = 'Настільна гра Strateg Карти мемчики та котики (30729)'
    dashboard.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    assert item_page.get_title() == title
