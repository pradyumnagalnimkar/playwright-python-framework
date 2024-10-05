from pages.base_page import BasePage

class DashboardPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.url = "/dashboard/index/"

        """WebElement Locators"""
