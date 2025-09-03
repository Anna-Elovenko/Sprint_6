from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class QuestionPage:
    
    title_question = (By.XPATH, "//span[text()='Вопросы о важном']")
    section_question = (By.CLASS_NAME, "accordion")
    question_1 = (By.XPATH, "//div[@class='accordion__button' and text()='Сколько это стоит? И как оплатить?']")
    question_2 = (By.XPATH, "//div[@class='accordion__button' and text()='Хочу сразу несколько самокатов! Так можно?']")
    question_3 = (By.XPATH, "//div[@class='accordion__button' and text()='Как рассчитывается время аренды?']")
    question_4 = (By.XPATH, "//div[@class='accordion__button' and text()='Можно ли заказать самокат прямо на сегодня?']")
    question_5 = (By.XPATH, "//div[@class='accordion__button' and text()='Можно ли продлить заказ или вернуть самокат раньше?']")
    question_6 = (By.XPATH, "//div[@class='accordion__button' and text()='Вы привозите зарядку вместе с самокатом?']")
    question_7 = (By.XPATH, "//div[@class='accordion__button' and text()='Можно ли отменить заказ?']")
    question_8 = (By.XPATH, "//div[@class='accordion__button' and text()='Я жизу за МКАДом, привезёте?']")
    answer_1 = (By.XPATH, "//div[@id='accordion__panel-0']")
    answer_2 = (By.XPATH, "//div[@id='accordion__panel-1']")
    answer_3 = (By.XPATH, "//div[@id='accordion__panel-2']")
    answer_4 = (By.XPATH, "//div[@id='accordion__panel-3']")
    answer_5 = (By.XPATH, "//div[@id='accordion__panel-4']")
    answer_6 = (By.XPATH, "//div[@id='accordion__panel-5']")
    answer_7 = (By.XPATH, "//div[@id='accordion__panel-6']")
    answer_8 = (By.XPATH, "//div[@id='accordion__panel-7']")

    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def scroll_to_element(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        return element
    
    def click_question_and_check_answer(self, question_locator, answer_locator):
        self.scroll_to_element(question_locator)
        self.wait.until(EC.element_to_be_clickable(question_locator)).click()
        return self.wait.until(EC.visibility_of_element_located(answer_locator)).is_displayed()
    