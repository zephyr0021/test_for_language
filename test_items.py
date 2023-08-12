import time

import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


def test_cart_button(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    time.sleep(10)
    cart_button = browser.find_element(By.CSS_SELECTOR, "#add_to_basket_form > button")
    assert cart_button is not None, "cart button is not exist"
