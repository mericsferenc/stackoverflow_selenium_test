from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class JavaScriptExecutorPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.home_url = self.base_url

    def navigate(self):
        """Navigate to the base URL."""
        self.navigate_to(self.home_url)

    def scroll_to_bottom(self):
        """Scroll to the bottom of the page using JavaScriptExecutor."""
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def get_scroll_position(self):
        """Return the current vertical scroll position."""
        return self.driver.execute_script("return window.pageYOffset;")
