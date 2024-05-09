import unittest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.home_page import HomePage
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

    def test_login_logout(self):
        login_page = LoginPage(self.driver)
        home_page = HomePage(self.driver)
        login_page.login(STACKOVERFLOW_EMAIL, STACKOVERFLOW_PASSWORD)
        if not home_page.is_user_logged_in():
            error_message = login_page.get_error_message()
            print(f"Login failed with error: {error_message}")
        self.assertTrue(home_page.is_user_logged_in(), "Login should be successful")

        home_page.logout()
        self.assertTrue(home_page.is_user_logged_out(), "Logout should be successful")

    def test_static_page_title(self):
        home_page = HomePage(self.driver)
        home_page.navigate()
        self.assertEqual(self.driver.title, "Stack Overflow - Where Developers Learn, Share, & Build Careers")

    def test_multiple_pages(self):
        home_page = HomePage(self.driver)
        urls = [
            "https://stackoverflow.com/questions",
            "https://stackoverflow.com/jobs",
            "https://stackoverflow.com/teams"
        ]
        for url in urls:
            home_page.navigate_to(url)
            self.assertTrue(self.driver.title)

if __name__ == '__main__':
    unittest.main()

# python -m unittest tests.test_suite