import time
from selenium.webdriver.common.by import By


def test_guest_can_see_add_to_basket_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(30)
    add_to_basket = browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")
    assert add_to_basket, 'No add to basket button.'
