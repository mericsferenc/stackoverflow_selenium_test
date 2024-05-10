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

    def add_consent_cookies(self):
        """Set the consent cookies to avoid showing the pop-up."""
        consent_cookies = [
            {
                'name': 'OptanonConsent',
                'value': ('isGpcEnabled=0&datestamp=Fri+May+10+2024+20%3A37%3A25+GMT%2B0200'
                          '+(k%C3%B6z%C3%A9p-eur%C3%B3pai+ny%C3%A1ri+id%C5%91)&version=202312.1.0&'
                          'isIABGlobal=false&hosts=&consentId=0443a6dd-dfa1-4281-b254-a81bd54d40fa&'
                          'interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1'
                          '%2CC0004%3A1%2CC0002%3A1&browserGpcFlag=0&geolocation=HU%3BZA&AwaitingReconsent=false'), # NOTE: should go to .env file like password, this is just for testing
                'domain': '.stackoverflow.com',
                'path': '/',
                'secure': True,
                'httpOnly': False
            },
            {
                'name': 'eupubconsent-v2',
                'value': 'CP4uyRgP4uyRgAcABBENAkEwAP_AAAAAACiQF5wBAAGAAgANAAvMAAAAgSACAvMdABAXmSgAgLzKQAQF5gAA.f_gAAAAAAAAA', # NOTE: should go to .env file like password, this is just for testing
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
