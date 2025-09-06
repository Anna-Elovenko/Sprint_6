import allure
from selenium import webdriver
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import urls, order_data


class TestOrder:

    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.main_page = MainPage(cls.driver)
        cls.order_page = OrderPage(cls.driver)

    @allure.title("Проверка оформления заказа через верхнюю кнопку")
    def test_order_from_top_button(self):
        self.main_page.open(urls.BASE_URL)
        self.main_page.click_top_order()
        self.order_page.fill_order_form(order_data.order_1)
        assert self.order_page.check_success_message(), "Модальное окно подтверждения не появилось после заказа (верхняя кнопка)"

    @allure.title("Проверка оформления заказа через нижнюю кнопку")
    def test_order_from_bottom_button(self):
        self.main_page.open(urls.BASE_URL)
        self.main_page.click_bottom_order()
        self.order_page.fill_order_form(order_data.order_2)
        assert self.order_page.check_success_message(), "Модальное окно подтверждения не появилось после заказа (нижняя кнопка)"

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
        