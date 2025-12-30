import allure

from task_2_2.pages.main_page import MainPage


class TestTaskOpen:
    main_page = MainPage()
    task_name = 'Реализация новой галереи изображений'
    status = 'InProgress'

    def test_task_open(self):
        with allure.step('Go to https://avito-tech-internship-psi.vercel.app'):
            assert self.main_page.is_opened(), 'Main page should be open.'

        with allure.step('Click on task: Реализация новой галереи изображений.'):
            self.main_page.click_on_task(self.task_name)

        with allure.step('Change status of task on InProgress. Click on Обновить.'):
            self.main_page.change_description_and_update(self.status)
