from task_2_2.elements.base_element import BaseElement


class BasePage:
    def __init__(self, name, locator):
        self.name = name
        self.locator = locator

    def is_opened(self):
        return BaseElement(self.name, self.locator).presence()
