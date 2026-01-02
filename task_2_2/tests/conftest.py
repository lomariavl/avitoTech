import pytest

from task_2_2.utils.singleton_driver import SingletonDriver
from task_2_2.resources.config import URL, BROWSER, WIDTH, HEIGHT


@pytest.fixture(scope='class', autouse=True)
def setup():
    driver = SingletonDriver(BROWSER).get_driver()
    driver.get(URL)
    driver.set_window_size(WIDTH, HEIGHT)
    yield driver
    SingletonDriver.quit_driver()
