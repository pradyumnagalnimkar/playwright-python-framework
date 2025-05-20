import allure

from pages.base_page import BasePage

class UserManagement(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.url = 'web/index.php/admin/viewSystemUsers'

        """WebElement Locators"""
        self.add_user_button = self.page.get_by_role("button", name="Add")
        self.user_role_dropdown = self.page.locator("//label[text()='User Role']/parent::div/following-sibling::div//div[contains(@class,'oxd-select-text--active')]")
        self.user_role_dropdown_value_admin = self.page.get_by_role("option", name="Admin").locator("span")
        self.user_role_dropdown_value_ess = self.page.get_by_role("option", name="ESS").locator("span")
        self.employee_name_textbox = self.page.get_by_placeholder('Type for hints...')
        self.status_dropdown = self.page.locator("//label[text()='Status']/parent::div/following-sibling::div//div[contains(@class,'oxd-select-text--active')]")
        self.status_dropdown_value_enabled= self.page.get_by_text('Enabled')
        self.status_dropdown_value_disabled = self.page.get_by_text('Disabled')
        self.username_textbox = self.page.locator("//label[text()='Username']/parent::div/following-sibling::div//input")
        self.password_textbox = self.page.locator("//label[text()='Password']/parent::div/following-sibling::div//input")
        self.confirm_password_textbox = self.page.locator("//label[text()='Confirm Password']/parent::div/following-sibling::div//input")
        self.save_button = self.page.get_by_role("button", name="Save", exact=False)
        self.cancel_button = self.page.get_by_role("button", name="Cancel",exact=False)
        self.notification_banner = self.page.locator("//div[contains(@class,'toast--success')]")
        self.notification_message = self.page.locator("//p[contains(@class,'toast-message')]")


    @allure.step("Action: Click on Add user button")
    def add_user(self):
        self.add_user_button.wait_for()
        self.add_user_button.click()

    @allure.step("Action: Create new user")
    def fill_user_details(self, user_role, employee_name, status, username, password):
        self.user_role_dropdown.click()
        self.page.get_by_role("option", name=user_role).locator("span").click()
        self.employee_name_textbox.fill(employee_name)
        self.page.get_by_text(employee_name, exact=False).click()
        self.status_dropdown.click()
        self.page.get_by_role("option", name='Enabled').locator("span").click() if status else self.page.get_by_role("option", name='Disabled').locator("span").click()
        self.username_textbox.fill(username)
        self.password_textbox.fill(password)
        self.confirm_password_textbox.fill(password)

    @allure.step("Action: Save user")
    def save_user(self):
        self.save_button.click()

    @allure.step("Action: Cancel save user")
    def cancel_save_user(self):
        self.cancel_button.click()