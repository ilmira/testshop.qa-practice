import pytest
from selenium import webdriver


@pytest.fixture(autouse=True)
def driver(request):
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
