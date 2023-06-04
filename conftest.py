import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en",
                     help="По дефолту язык английский")


@pytest.fixture(scope="function")
def browser(request):

    print("\nstart browser..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()