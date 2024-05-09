from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class TextareaPage(BasePage):
    TEXTAREA = (By.ID, 'id-of-textarea')

    def fill_textarea(self, content):
        textarea = self.find_element(self.TEXTAREA)
        textarea.clear()
        textarea.send_keys(content)

    def get_textarea_content(self):
        return self.find_element(self.TEXTAREA).get_attribute('value')
