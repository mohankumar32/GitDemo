import pytest
from selenium import webdriver


@pytest.fixture()

def setUp(request):
    driver = webdriver.Chrome(executable_path="c:\\chromedriver.exe")
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    yield
    driver.close()