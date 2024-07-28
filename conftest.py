import pytest
from utils.logger.logger import Logger

@pytest.fixture(scope="session")
def logger():
    return Logger()