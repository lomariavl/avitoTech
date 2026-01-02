import allure

from task_2_2.pages.main_page import MainPage
from task_2_2.utils.data_manager import DataManager


class TestCheckTaskCreated:
    main_page = MainPage()
    test_data = DataManager().get_test_data().new_task

    def test_check_task_created(self):
        with allure.step('Go to https://avito-tech-internship-psi.vercel.app'):
            assert self.main_page.is_opened(), 'Main page should be open.'

        with allure.step('Click on button Create task.'):
            assert self.main_page.go_to_create_task(), 'Menu was not found.'

        with allure.step('Fill in all fields. Click on Create.'):
            self.main_page.fill_in_and_click(self.test_data.task_name, self.test_data.task_description)
