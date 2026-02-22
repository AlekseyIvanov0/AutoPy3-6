import pytest
from selenium.webdriver.common.by import By 


LINK = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

class TestCatalog():
    def test_add_cart_btn(self, browser):
        browser.get(LINK)
        add_to_cart_btn = browser.find_elements(By.CLASS_NAME,'btn-add-to-basket')
        print(add_to_cart_btn)
        assert len(add_to_cart_btn) == 1, (
            'Кнопки "Добавить в корзину" нет или их несколько'
        )
