import os

from pages.base_page import  BasePage

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.url = "/"

        """WebElement Locators"""
        self.username_textbox = self.page.get_by_placeholder("Username")
        self.password_textbox = self.page.get_by_placeholder("Password")
        self.login_button = self.page.get_by_role("button", name="Login")

    def login(self, username, password):
        self.username_textbox.wait_for()
        self.username_textbox.fill(username)
        self.password_textbox.fill(password)
        self.login_button.click()

