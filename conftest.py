import time

import pytest
from selenium import webdriver


@pytest.fixture(autouse=True)
def driver(request):
    driver = webdriver.Chrome()
    time.sleep(30)
    yield driver
    time.sleep(10)
    driver.quit()
