import logging

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.core.os_manager import ChromeType


class BrowserFactory:
    @staticmethod
    def get_driver(browser_name):
        match browser_name.lower():
            case 'firefox':
                options = webdriver.FirefoxOptions()
                options.page_load_strategy = 'eager'
                return webdriver.Firefox(options=options)
            case 'chromium':
                options = webdriver.ChromeOptions()
                options.add_argument('--incognito')
                options.page_load_strategy = 'eager'
                return webdriver.Chrome(service=ChromiumService(ChromeDriverManager(
                    chrome_type=ChromeType.CHROMIUM).install()), options=options)
            case _:
                logging.error(f'Unsupported browser: {browser_name}.')
