
import logging
import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def get_logger(name, file_path):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler = logging.FileHandler(file_path, mode='w')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger


@pytest.fixture(scope="function")
def logger(request):
    test_name = request.node.name
    log_dir = os.path.join(os.getcwd(), "opencart_logs")
    os.makedirs(log_dir, exist_ok=True)
    log_file_path = os.path.join(log_dir, f"{test_name}.log")
    return get_logger(test_name, log_file_path)


@pytest.fixture(scope="session")
def driver(request):
    browser = request.config.getoption("--browser")
    remote_url = request.config.getoption("--remote-url")

    if browser == "chrome":
        options = Options()
        # browser = webdriver.Chrome(service=service, options=options)
        options = Options()
    elif browser == "firefox":
        options = FirefoxOptions()
        # browser = webdriver.Firefox(service=service, options=options)
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    (options.set_capability("browserVersion", os.getenv("VERSION")))
    selenoid_options = {
        "enableVideo": True,
        "enableVNC": True,
        "videoName": f"{os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0]}.mp4",
        "name": os.environ.get("PYTEST_CURRENT_TEST").split(":")[-1].split(" ")[0]
    }
    options.set_capability("selenoid:options", selenoid_options)
    executor_url = "http://localhost:4444/wd/hub/"
    base_url = f"https://demo-opencart.ru/"
    driver = webdriver.Remote(
        command_executor=executor_url,
        options=options,
    )
    driver.get(base_url)

    yield driver
    driver.quit()

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="browser to use: chrome or firefox")
    parser.addoption("--remote-url", action="store", default="http://localhost:4444/wd/hub/", help="remote URL for Selenoid")