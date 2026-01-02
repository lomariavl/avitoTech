import logging

import allure

from task_2_2.pages.main_page import MainPage
from task_2_2.utils.data_manager import DataManager


class TestBoardOfProjectOpen:
    main_page = MainPage()
    test_data = DataManager().get_test_data().existing_task

    def test_board_of_project_open(self):
        with allure.step('Go to https://avito-tech-internship-psi.vercel.app'):
            assert self.main_page.is_opened(), 'Main page should be open.'
            logging.info('Main page opened.')

        with allure.step('Choose on task and go to board.'):
            self.main_page.click_on_task(self.test_data.task_name)
            logging.info('Task opened.')
            self.main_page.go_to_board()
            logging.info('Board opened.')
            assert self.main_page.fields_match(self.test_data.task_name, self.test_data.task_description,
                                               self.test_data.executor), 'Fields task should be matched.'
