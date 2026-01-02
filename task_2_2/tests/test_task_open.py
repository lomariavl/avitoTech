import allure

from task_2_2.pages.main_page import MainPage
from task_2_2.utils.data_manager import DataManager


class TestTaskOpen:
    main_page = MainPage()
    existing_task = DataManager().get_test_data().existing_task
    new_task = DataManager().get_test_data().new_task

    def test_task_open(self):
        with allure.step('Go to https://avito-tech-internship-psi.vercel.app'):
            assert self.main_page.is_opened(), 'Main page should be open.'

        with allure.step('Click on task: Реализация новой галереи изображений.'):
            self.main_page.click_on_task(self.existing_task.task_name)

        with allure.step('Change status of task on InProgress. Click on Обновить.'):
            self.main_page.change_status_and_update(self.new_task.status)
