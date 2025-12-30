import allure

from task_2_2.pages.main_page import MainPage


class TestCheckTaskCreated:
    main_page = MainPage()
    task_name = 'NAME'
    task_description = 'Description'

    def test_check_task_created(self):
        with allure.step('Go to https://avito-tech-internship-psi.vercel.app/issues'):
            assert self.main_page.is_opened(), 'Main page should be open.'

        with allure.step('Click on button Create task.'):
            assert self.main_page.go_to_create_task(), 'Menu was not found.'

        with allure.step('Fill in all fields. Click on Create.'):
            self.main_page.fill_in_and_click(self.task_name, self.task_description)
