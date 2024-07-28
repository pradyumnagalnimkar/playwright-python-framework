from playwright.sync_api import Page, expect
def test_login(page: Page, logger):
    username, password = "Admin", "admin123"
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    logger.info("Successfully navigated to OrangeHRM landing page")
    page.get_by_placeholder("Username").fill("Admin")
    page.get_by_placeholder("Password").fill("admin123")
    page.get_by_role("button", name="Login").click()
    page.wait_for_selector("//span[@class='oxd-userdropdown-tab']")
    if page.locator("//span[@class='oxd-userdropdown-tab']").is_visible():
        logger.info(f"Logged in successfully with {username} & {password}.")
    else:
        logger.error(f"Error logging in with {username} & {password}")
