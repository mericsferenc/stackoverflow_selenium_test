from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class JavaScriptExecutorPage(BasePage):
    FOOTER_LOCATOR = (By.ID, "footer")

    def __init__(self, driver):
        super().__init__(driver)
        self.home_url = self.base_url

    def navigate(self):
        """Navigate to the base URL."""
        self.navigate_to(self.home_url)

    def wait_for_page_load(self, timeout=15):
        """Wait for the footer to appear to ensure the page is fully loaded."""
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(self.FOOTER_LOCATOR)
        )

    def scroll_to_bottom(self):
        """Scroll to the bottom of the page using JavaScriptExecutor."""
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def get_scroll_position(self):
        """Return the current vertical scroll position."""
        return self.driver.execute_script("return window.pageYOffset;")
