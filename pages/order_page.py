from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class OrderPage:

    first_name = (By.XPATH, "//input[@placeholder='* Имя']")
    last_name = (By.XPATH, "//input[@placeholder='* Фамилия']")
    address = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    metro_station = (By.CLASS_NAME, "select-search__input")
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
    
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def fill_order_form(self, data):
        self.driver.find_element(*self.first_name).send_keys(data["first_name"])
        self.driver.find_element(*self.last_name).send_keys(data["last_name"])
        self.driver.find_element(*self.address).send_keys(data["address"])

        self.driver.find_element(*self.metro_station).send_keys(data["station"])
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "select-search__option"))).click()
        
        self.driver.find_element(*self.phone).send_keys(data["phone"])
        self.driver.find_element(*self.next_button).click()

        date_input = self.driver.find_element(*self.date)
        date_input.send_keys(data["date"])
        date_input.send_keys(Keys.ESCAPE)
        
        self.wait.until(EC.element_to_be_clickable(self.rental_duration)).click()
        self.wait.until(EC.element_to_be_clickable(self.rental_day_option)).click()

        self.driver.find_element(*self.color_black).click()
        self.driver.find_element(*self.comment).send_keys(data["comment"])
        self.driver.find_element(*self.order_button).click()
        self.wait.until(EC.element_to_be_clickable(self.confirm_button)).click()


    def is_success_message_visible(self):
        return self.wait.until(EC.visibility_of_element_located(self.success_modal)).is_displayed()
