from task_2_2.elements.base_element import BaseElement
from task_2_2.pages.base_page import BasePage


class MainPage(BasePage):
    BUTTON_CREATE_TASK = BaseElement('Create Task', "//button[contains(text(),'Создать задачу')]")
    DOM_ELEMENT = BaseElement('Create Task', "//h5[contains(text(),'Создание')]")
    NAME = BaseElement('Name',
                       "//span[contains(text(),'Название')]//ancestor::*[contains(@class,'MuiInputBase-root')]//input")
    DESCRIPTION = BaseElement('Description',
                              "//span[contains(text(),'Описание')]//ancestor::*[contains(@class,'MuiInputBase-root')]//textarea")
    CHECKLIST_LOCATOR = "//*[contains(*//text(),'{}') and *//@id='select-label']"
    BUTTON_LOCATOR = "//button[text()='{}']"
    PROJECT = BaseElement('Project', "//li[contains(text(),'Редизайн карточки товара')]")
    PRIORITY = BaseElement('Priority', "//li[contains(text(),'Low')]")
    EXECUTOR = BaseElement('Executor', "//li[contains(text(),'Александра Ветрова')]")
    MENU_LOCATOR = "//*[@id='menu-']"
    CURRENT_TASK = "//h6[contains(text(),'{}')]"
    STATUS = "//li[contains(text(),'{}')]"
    SEARCH = BaseElement('Search', "//input[contains(@placeholder,'Поиск')]")
    LINK = BaseElement('Перейти на доску', "//a[contains(text(),'Перейти')]")
    DESCRIPTION_CURRENT_TASK = "//p[contains(text(),'{}')]"
    CURRENT_EXECUTOR = "//span[contains(text(), '{}')]"

    def __init__(self):
        super().__init__('Main page', "//*[contains(text(),'Список задач')]")

    def go_to_create_task(self) -> bool:
        self.BUTTON_CREATE_TASK.click()
        return self.DOM_ELEMENT.presence()

    def fill_in_and_click(self, name, description) -> None:
        self.NAME.send_key(name)
        self.DESCRIPTION.send_key(description)
        BaseElement('Проект', self.CHECKLIST_LOCATOR.format('Проект')).click()
        self.PROJECT.click()
        BaseElement('Приоритет', self.CHECKLIST_LOCATOR.format('Приоритет')).click(blocking_locator=self.MENU_LOCATOR)
        self.PRIORITY.click()
        BaseElement('Исполнитель', self.CHECKLIST_LOCATOR.format('Исполнитель')).click(
            blocking_locator=self.MENU_LOCATOR)
        self.EXECUTOR.click()
        BaseElement('Создать', self.BUTTON_LOCATOR.format('Создать')).click(blocking_locator=self.MENU_LOCATOR)

    def click_on_task(self, task):
        BaseElement(task, self.CURRENT_TASK.format(task)).click()

    def change_description_and_update(self, status) -> None:
        BaseElement('Статус', self.CHECKLIST_LOCATOR.format('Статус')).click()
        BaseElement(status, self.STATUS.format(status)).click()
        BaseElement('Обновить', self.BUTTON_LOCATOR.format('Обновить')).click(blocking_locator=self.MENU_LOCATOR)

    def search_task(self, information) -> int:
        self.SEARCH.send_key(information)
        return BaseElement(information, self.CURRENT_TASK.format(information)).presence()

    def go_to_board(self) -> None:
        self.LINK.click()

    def fields_match(self, task_name, task_description, executor) -> bool:
        return (
                BaseElement(task_name, self.CURRENT_TASK.format(task_name)).presence()
                and BaseElement(task_description, self.DESCRIPTION_CURRENT_TASK.format(task_description)).presence()
                and BaseElement(executor, self.CURRENT_EXECUTOR.format(executor)).presence()
        )
