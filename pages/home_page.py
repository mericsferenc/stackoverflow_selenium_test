from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    USER_MENU = (By.XPATH, "//div[contains(@class, 's-user-card')]")
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Log out']")
    LOGOUT_URL = "https://stackoverflow.com/users/logout"
    LOGGED_OUT_MESSAGE = (By.XPATH, "//a[@href='/users/login']")

    def __init__(self, driver):
        super().__init__(driver)
        self.home_url = self.base_url

    def navigate(self):
        self.navigate_to(self.home_url)

    def is_user_logged_in(self):
        return self.find_element(self.USER_MENU) is not None

    def logout(self):
        self.navigate_to(self.LOGOUT_URL)
        logout_button = self.find_element(self.LOGOUT_BUTTON)
        if logout_button:
            logout_button.click()

    def is_user_logged_out(self):
        return self.find_element(self.LOGGED_OUT_MESSAGE) is not None
