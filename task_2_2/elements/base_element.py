from task_2_2.utils.driver_utils import DriverUtils


class BaseElement:
    def __init__(self, name, locator):
        self.name = name
        self.locator = locator

    def presence(self):
        return DriverUtils.is_element_presence(self.locator)

    def click(self, blocking_locator: str = None):
        DriverUtils.click(self.locator, blocking_locator)

    def send_key(self, key):
        DriverUtils.send(self.locator, key)
