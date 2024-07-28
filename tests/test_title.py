from playwright.sync_api import Page, expect

def test_title(page: Page, logger):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    logger.info("Navigated to OrangeHRM page")
    expect(page).to_have_title("OrangeHRM")
    if page.title() == "OrangeHRM":
        logger.info(f"Validated OrangeHRM page title")
    else:
        logger.error(f"Actual title: {page.title()}, Expected title: OrangeHR")