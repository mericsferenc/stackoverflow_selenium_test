from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class DropdownPage(BasePage):
    DEPARTMENT_SELECT = (By.CSS_SELECTOR, "select.fs-body3")
    OPTION_SALES = (By.XPATH, "//option[contains(text(), 'Sales')]")

    def navigate(self):
        """Navigate to the Work Here page."""
        self.navigate_to("https://stackoverflow.co/company/work-here/")

    def select_sales_option(self):
        """Select the 'Sales (1)' option from the dropdown."""
        department_select = self.find_element(self.DEPARTMENT_SELECT)
        department_select.click()  # Open the dropdown
        sales_option = self.find_element(self.OPTION_SALES)
        sales_option.click()
