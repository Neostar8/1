import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options

@pytest.fixture()
def get_chrome_options():
    options = chrome_options()
    options.add_argument('chrome')
    # options.add_argument('--hedless')
    options.add_argument('--start-maximized')
    options.add_argument('--window-size=1500,1000')
    return options

@pytest.fixture(scope='function') #'session'использует один веб драйвер

def get_webdriver(get_chrome_options):
    options = get_chrome_options
    driver = webdriver.Chrome(options=options)
    return driver

@pytest.fixture
def setup(request, get_webdriver):
    driver = get_webdriver
    url = 'https://www.citilink.ru/'
    if request.cls is not None:
        request.cls.driver = driver
    driver.get(url)
    yield driver
    driver.quit()

@pytest.fixture(autouse=True)
def setup(request, get_webdriver):
    driver = get_webdriver
    url = 'https://www.citilink.ru/'
    if request.cls is not None:
        request.cls.driver = driver
    driver.get(url)
    yield driver
    driver.quit()


