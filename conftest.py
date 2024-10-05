import os
import pytest

from pages.login_page import LoginPage
from utils.logger.logger import Logger

@pytest.fixture(scope="session")
def logger():
    return Logger()

@pytest.fixture(autouse=True)
def login_to_app(page):
    login_page = LoginPage(page)
    login_page.load()
    login_page.login(os.getenv('USERNAME'), os.getenv('PASSWORD'))

