import allure

from task_2_2.pages.main_page import MainPage
from task_2_2.utils.data_manager import DataManager


class TestTaskSearch:
    main_page = MainPage()
    test_data = DataManager().get_test_data().existing_task

    def test_task_search(self):
        with allure.step('Go to https://avito-tech-internship-psi.vercel.app'):
            assert self.main_page.is_opened(), 'Main page should be open.'

        with allure.step('Enter in search field name of task'):
            assert self.main_page.search_task(self.test_data.task_name), 'Task was not found in the list.'
