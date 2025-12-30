import logging

from selenium.webdriver.remote.webdriver import WebDriver

from task_2_2.utils.browser_factory import BrowserFactory


class SingletonDriver:
    _instance: 'SingletonDriver' = None
    _browser_name: str
    _driver: WebDriver = None

    def __new__(cls, browser_name: str):
        if not cls._instance:
            cls._browser_name = browser_name
            cls._instance = super(SingletonDriver, cls).__new__(cls)
        return cls._instance

    @classmethod
    def get_driver(cls):
        if not cls._instance._driver:
            logging.info('Creating new driver')
            cls._instance._driver = BrowserFactory.get_driver(cls._browser_name)
        return cls._instance._driver

    @classmethod
    def quit_driver(cls):
        if cls._instance._driver is not None:
            cls._instance._driver.quit()
            cls._instance._driver = None
            logging.info('The driver stopped')
