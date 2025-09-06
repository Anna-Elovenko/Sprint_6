import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage


class OrderPage(BasePage):

    first_name = (By.XPATH, "//input[@placeholder='* Имя']")
    last_name = (By.XPATH, "//input[@placeholder='* Фамилия']")
    address = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    metro_station = (By.CLASS_NAME, "select-search__input")
    metro_option = (By.CLASS_NAME, "select-search__option")
    phone = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    next_button = (By.XPATH, "//button[text()='Далее']")

    date = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    rental_duration = (By.CLASS_NAME, "Dropdown-control")
    rental_day_option = (By.XPATH, "//div[text()='двое суток']")
    color_black = (By.ID, "black")
    comment = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    order_button = (By.XPATH, "(//button[text()='Заказать'])[2]")
    confirm_button = (By.XPATH, "//button[contains(text(), 'Да')]")
    success_modal = (By.CLASS_NAME, "Order_ModalHeader__3FDaJ")

    @allure.step("Заполняем форму заказа")
    def fill_order_form(self, data):
        self.send_keys(self.first_name, data["first_name"])
        self.send_keys(self.last_name, data["last_name"])
        self.send_keys(self.address, data["address"])

        self.send_keys(self.metro_station, data["station"])
        self.wait_for_element_present(self.metro_option).click()

        self.send_keys(self.phone, data["phone"])
        self.click(self.next_button)

        self.send_keys(self.date, data["date"])
        self.find(self.date).send_keys(Keys.ESCAPE)

        self.click(self.rental_duration)
        self.click(self.rental_day_option)

        self.click(self.color_black)
        self.send_keys(self.comment, data["comment"])
        self.click(self.order_button)
        self.click(self.confirm_button)

    @allure.step("Проверяем успешное отображение модального окна подтверждения заказа")
    def check_success_message(self):
        return self.wait_for_element_visible(self.success_modal).is_displayed()

