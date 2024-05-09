from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    USERNAME_INPUT = (By.ID, 'email')
    PASSWORD_INPUT = (By.ID, 'password')
    LOGIN_BUTTON = (By.ID, 'submit-button')
    ERROR_MESSAGE = (By.CLASS_NAME, 'js-error-message')

    def __init__(self, driver):
        super().__init__(driver)
        self.login_url = f"{self.base_url}/users/login"

    def navigate(self):
        self.navigate_to(self.login_url)

    def set_username(self, username):
        self.find_element(self.USERNAME_INPUT).send_keys(username)

    def set_password(self, password):
        self.find_element(self.PASSWORD_INPUT).send_keys(password)

    def click_login(self):
        self.find_element(self.LOGIN_BUTTON).click()

    def login(self, username, password):
        self.navigate()
        self.set_username(username)
        self.set_password(password)
        self.click_login()

    def get_error_message(self):
        return self.find_element(self.ERROR_MESSAGE).text if self.find_element(self.ERROR_MESSAGE) else None
