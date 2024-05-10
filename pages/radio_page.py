from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class RadioPage(BasePage):
    RADIO_ACCOUNT_ISSUE = (By.ID, 'group-0')
    COOKIE_CONSENT_BUTTON = (By.XPATH, "//button[contains(text(), 'Accept all cookies')]")

    def navigate(self):
        self.navigate_to("https://stackoverflow.com/contact")

    def accept_all_cookies(self):
        try:
            cookie_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.COOKIE_CONSENT_BUTTON)
            )
            cookie_button.click()
        except Exception:
            pass  # Ignore if the button isn't present

    def select_account_issue(self):
        self.accept_all_cookies()
        radio_button = self.find_element(self.RADIO_ACCOUNT_ISSUE)
        if radio_button and not radio_button.is_selected():
            self.scroll_into_view(radio_button)
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.RADIO_ACCOUNT_ISSUE)
            ).click()

    def is_account_issue_selected(self):
        radio_button = self.find_element(self.RADIO_ACCOUNT_ISSUE)
        return radio_button.is_selected() if radio_button else False

    def scroll_into_view(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
