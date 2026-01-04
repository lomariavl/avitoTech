import logging

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from task_2_2.utils.singleton_driver import SingletonDriver
from task_2_2.resources.config import TIMEOUT


class DriverUtils:
    @staticmethod
    def get_driver_for_wait():
        driver = SingletonDriver.get_driver()
        return WebDriverWait(driver, TIMEOUT)

    @staticmethod
    def is_element_presence(locator) -> bool:
        try:
            DriverUtils.get_driver_for_wait().until(
                EC.presence_of_element_located(
                    (By.XPATH, locator)
                )
            )
            return True
        except TimeoutException:
            logging.warning(f'The waiting time for the \'{locator}\' has expired.')
            return False

    @staticmethod
    def wait_until_not_obscured(blocking_locator):
        DriverUtils.get_driver_for_wait().until(
            EC.invisibility_of_element_located((By.XPATH, blocking_locator))
        )

    @staticmethod
    def click(locator, blocking_locator: str = None):
        try:
            if blocking_locator:
                DriverUtils.wait_until_not_obscured(blocking_locator)
            DriverUtils.get_driver_for_wait().until(EC.element_to_be_clickable((By.XPATH, locator))).click()
            logging.info(f'The element \'{locator}\' was clicked.')
        except TimeoutException as e:
            logging.error(f'The waiting time for the \'{locator}\' has expired. Failed to click, {e}')

    @staticmethod
    def send(locator, key):
        if DriverUtils.is_element_presence(locator):
            return SingletonDriver.get_driver().find_element(By.XPATH, locator).send_keys(key)
