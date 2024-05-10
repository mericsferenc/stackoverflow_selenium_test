import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.dropdown_page import DropdownPage
from pages.radio_page import RadioPage
from pages.textarea_page import TextareaPage
from pages.ask_question_page import AskQuestionPage
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
STACKOVERFLOW_EMAIL = os.getenv('STACKOVERFLOW_EMAIL')
STACKOVERFLOW_PASSWORD = os.getenv('STACKOVERFLOW_PASSWORD')

class StackOverflowTestSuite(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    # def test_login_logout(self):
    #     login_page = LoginPage(self.driver)
    #     home_page = HomePage(self.driver)
    #     login_page.login(STACKOVERFLOW_EMAIL, STACKOVERFLOW_PASSWORD)
    #     if not home_page.is_user_logged_in():
    #         error_message = login_page.get_error_message()
    #         print(f"Login failed with error: {error_message}")
    #     self.assertTrue(home_page.is_user_logged_in(), "Login should be successful")

    #     home_page.logout()
    #     self.assertTrue(home_page.is_user_logged_out(), "Logout should be successful")

    # def test_static_page_title(self):
    #     home_page = HomePage(self.driver)
    #     home_page.navigate()
    #     self.assertEqual(self.driver.title, "Stack Overflow - Where Developers Learn, Share, & Build Careers")

    def test_multiple_pages(self):
        home_page = HomePage(self.driver)
        pages = [
            {
                "url": "https://stackoverflow.co/teams/use-cases/engineering/",
                "expected_text": "Build an efficient knowledge sharing culture"
            },
            {
                "url": "https://stackoverflow.co/teams/use-cases/data-analytics/",
                "expected_text": "We’ll organize the data, so you can do the science."
            },
            {
                "url": "https://stackoverflow.co/teams/use-cases/devops/",
                "expected_text": "Your system handles millions of interrupts, but you shouldn't have to."
            },
            {
                "url": "https://stackoverflow.co/teams/use-cases/customer-support/",
                "expected_text": "Leave no support question unanswered."
            }
        ]

        for page in pages:
            home_page.navigate_to(page["url"])
            self.assertIn(page["expected_text"], self.driver.page_source)

    # def test_complex_xpath(self):
    #     home_page = HomePage(self.driver)
    #     home_page.navigate()
    #     complex_element = home_page.find_element((By.XPATH, "//div//a[@href='/questions']"))
    #     self.assertTrue(complex_element, "Complex XPath element should be found")

    # def test_explicit_wait(self):
    #     home_page = HomePage(self.driver)
    #     home_page.navigate()
    #     element = home_page.find_element((By.XPATH, "//a[contains(@href, '/questions')]"), timeout=15)
    #     self.assertTrue(element, "Element should be present with explicit wait")

    # def test_form_sending_with_user(self):
    #     login_page = LoginPage(self.driver)
    #     ask_question_page = AskQuestionPage(self.driver)
    #     login_page.login(STACKOVERFLOW_EMAIL, STACKOVERFLOW_PASSWORD)
    #     ask_question_page.navigate()
    #     ask_question_page.click_ask_question()
    #     ask_question_page.accept_all_cookies()
    #     ask_question_page.set_title("Sample Question Title")
    #     ask_question_page.click_next()
    
    # def test_radio_button_interaction(self):
    #     radio_page = RadioPage(self.driver)
    #     radio_page.navigate()
    #     radio_page.select_account_issue()
    #     self.assertTrue(radio_page.is_account_issue_selected(), "Radio button Account Issue should be selected")

if __name__ == '__main__':
    unittest.main()
