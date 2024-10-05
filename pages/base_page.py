import os
from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page

        """WebElement Locators"""
        self.dashboard_link = self.page.locator("//span[text()='Dashboard']")
        self.leave_link = self.page.locator("//span[text()='Leave']")

    def load(self):
        self.page.goto(self.url)


