from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class AskQuestionPage(BasePage):
    ASK_QUESTION_BUTTON = (By.CSS_SELECTOR, "a[href='/questions/ask']")
    TITLE_INPUT = (By.ID, 'title')
    NEXT_BUTTON = (By.XPATH, "//button[contains(text(), 'Next')]")
    COOKIE_CONSENT = (By.XPATH, "//button[contains(text(), 'Accept all cookies')]")

    OPTANON_CONSENT = os.getenv('OPTANON_CONSENT')
    EUPUBCONSENT_V2 = os.getenv('EUPUBCONSENT_V2')

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

    def add_consent_cookies(self):
        """Set the consent cookies to avoid showing the pop-up."""
        consent_cookies = [
            {
                'name': 'OptanonConsent',
                'value': self.OPTANON_CONSENT,
                'domain': '.stackoverflow.com',
                'path': '/',
                'secure': True,
                'httpOnly': False
            },
            {
                'name': 'eupubconsent-v2',
                'value': self.EUPUBCONSENT_V2,
                'domain': '.stackoverflow.com',
                'path': '/',
                'secure': True,
                'httpOnly': False
            }
        ]
        for cookie in consent_cookies:
            self.driver.add_cookie(cookie)

    def avoid_cookie_consent_popup(self):
        """Avoid cookie consent pop-up by adding consent cookies manually."""
        self.navigate()
        self.add_consent_cookies()
        self.driver.refresh()
