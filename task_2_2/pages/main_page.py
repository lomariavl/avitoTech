from task_2_2.elements.base_element import BaseElement
from task_2_2.models.for_test_data import FieldsForFillIn
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
    TASK_FIELD = "//li[contains(text(),'{}')]"
    MENU_LOCATOR = "//*[@id='menu-']"
    CURRENT_TASK = "//h6[contains(text(),'{}')]"
    SEARCH = BaseElement('Search', "//input[contains(@placeholder,'Поиск')]")
    LINK = BaseElement('Перейти на доску', "//a[contains(text(),'Перейти')]")
    DESCRIPTION_CURRENT_TASK = "//p[contains(text(),'{}')]"
    CURRENT_EXECUTOR = "//span[contains(text(), '{}')]"

    def __init__(self):
        super().__init__('Main page', "//*[contains(text(),'Список задач')]")

    def go_to_create_task(self) -> bool:
        self.BUTTON_CREATE_TASK.click()
        return self.DOM_ELEMENT.presence()

    def fill_in_and_click(self, name, description, project, priority, executor,
                          fields_for_fill_in: FieldsForFillIn) -> None:
        self.NAME.send_key(name)
        self.DESCRIPTION.send_key(description)
        BaseElement('Project', self.CHECKLIST_LOCATOR.format(fields_for_fill_in.project)).click()
        BaseElement('Project', self.TASK_FIELD.format(project)).click()
        BaseElement('Priority', self.CHECKLIST_LOCATOR.format(fields_for_fill_in.priority)).click(
            blocking_locator=self.MENU_LOCATOR)
        BaseElement('Priority', self.TASK_FIELD.format(priority)).click()
        BaseElement('Executor', self.CHECKLIST_LOCATOR.format(fields_for_fill_in.executor)).click(
            blocking_locator=self.MENU_LOCATOR)
        BaseElement('Executor', self.TASK_FIELD.format(executor)).click()
        BaseElement('Create', self.BUTTON_LOCATOR.format(fields_for_fill_in.create)).click(
            blocking_locator=self.MENU_LOCATOR)

    def click_on_task(self, task):
        BaseElement(task, self.CURRENT_TASK.format(task)).click()

    def change_status_and_update(self, status, fields_for_fill_in: FieldsForFillIn) -> None:
        BaseElement('Status', self.CHECKLIST_LOCATOR.format(fields_for_fill_in.status)).click()
        BaseElement(status, self.TASK_FIELD.format(status)).click()
        BaseElement('Update', self.BUTTON_LOCATOR.format(fields_for_fill_in.update)).click(blocking_locator=self.MENU_LOCATOR)

    def search_task(self, task_name) -> int:
        self.SEARCH.send_key(task_name)
        return BaseElement(task_name, self.CURRENT_TASK.format(task_name)).presence()

    def go_to_board(self) -> None:
        self.LINK.click()

    def fields_match(self, task_name, task_description, executor) -> bool:
        return (
                BaseElement(task_name, self.CURRENT_TASK.format(task_name)).presence()
                and BaseElement(task_description, self.DESCRIPTION_CURRENT_TASK.format(task_description)).presence()
                and BaseElement(executor, self.CURRENT_EXECUTOR.format(executor)).presence()
        )
