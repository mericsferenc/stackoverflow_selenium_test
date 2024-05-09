from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class DropdownPage(BasePage):
    FOLLOW_US_BUTTON = (By.CSS_SELECTOR, "button[aria-label='Follow us']")
    DROPDOWN_ITEMS = (By.XPATH, "//div[@role='menu']/a")

    def navigate(self):
        self.navigate_to("https://stackoverflow.co/")

    def open_dropdown(self):
        follow_us_button = self.find_element(self.FOLLOW_US_BUTTON)
        if follow_us_button:
            follow_us_button.click()
        else:
            raise ValueError("Follow us button not found")

    def select_option(self, option_text):
        dropdown_items = self.find_elements(self.DROPDOWN_ITEMS)
        if dropdown_items:
            for item in dropdown_items:
                if item.text.strip() == option_text:
                    item.click()
                    return
            raise ValueError(f"Option '{option_text}' not found in the dropdown")
        else:
            raise ValueError("Dropdown items not found")
