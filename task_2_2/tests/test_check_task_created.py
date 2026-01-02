import allure

from task_2_2.pages.main_page import MainPage
from task_2_2.utils.data_manager import DataManager


class TestCheckTaskCreated:
    main_page = MainPage()
    test_data = DataManager().get_test_data()
    new_task = test_data.new_task
    fields_for_fill_in = test_data.fields_for_fill_in

    def test_check_task_created(self):
        with allure.step('Go to https://avito-tech-internship-psi.vercel.app'):
            assert self.main_page.is_opened(), 'Main page should be open.'

        with allure.step('Click on button Create task.'):
            assert self.main_page.go_to_create_task(), 'Menu was not found.'

        with allure.step('Fill in all fields. Click on Create.'):
            self.main_page.fill_in_and_click(self.new_task.task_name, self.new_task.task_description,
                                             self.new_task.project, self.new_task.priority, self.new_task.executor,
                                             self.fields_for_fill_in)

            assert self.main_page.search_task(self.new_task.task_name), 'Fields task should be searched.'
