import pytest

from task_2_2.utils.singleton_driver import SingletonDriver

url = 'https://avito-tech-internship-psi.vercel.app'


@pytest.fixture(scope='class', autouse=True)
def setup():
    driver = SingletonDriver('firefox').get_driver()
    driver.get(url)
    driver.set_window_size(1920, 1020)
    yield driver
    SingletonDriver.quit_driver()
