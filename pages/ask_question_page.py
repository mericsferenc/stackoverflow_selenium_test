from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class AskQuestionPage(BasePage):
    ASK_QUESTION_BUTTON = (By.CSS_SELECTOR, "a[href='/questions/ask']")
    TITLE_INPUT = (By.ID, 'title')
    NEXT_BUTTON = (By.XPATH, "//button[contains(text(), 'Next')]")
    COOKIE_CONSENT = (By.XPATH, "//button[contains(text(), 'Accept all cookies')]")

    def navigate(self):
        self.navigate_to("https://stackoverflow.com")

    def click_ask_question(self):
        ask_question_button = self.find_element(self.ASK_QUESTION_BUTTON)
        if ask_question_button:
            ask_question_button.click()
        else:
            raise ValueError("Ask Question button not found")

    def set_title(self, title):
        title_input = self.find_element(self.TITLE_INPUT)
        if title_input:
            title_input.send_keys(title)
        else:
            raise ValueError("Title input not found")

    def click_next(self):
        self.wait_until_clickable(self.NEXT_BUTTON).click()

    def wait_until_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def accept_all_cookies(self):
        try:
            cookie_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.COOKIE_CONSENT)
            )
            cookie_button.click()
        except Exception:
            pass