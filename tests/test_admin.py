from playwright.sync_api import expect
from pages.admin.user_management_page import UserManagement


def test_crud_on_users(page, test_data):
    user_role, employee_name, status, username, password = test_data["user_role"], test_data["employee_name"], test_data["status"], test_data["username"], test_data["password"]
    user_management = UserManagement(page)
    user_management.load()
    user_management.add_user()
    user_management.fill_user_details(user_role, employee_name, status, username, password)
    user_management.save_user()
    expect(user_management.notification_message).to_contain_text('Successfully Saved', use_inner_text=True)
    expect(user_management.notification_banner).to_be_visible()