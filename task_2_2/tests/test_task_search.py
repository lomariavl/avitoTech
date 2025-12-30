import allure

from task_2_2.pages.main_page import MainPage


class TestTaskSearch:
    main_page = MainPage()

    def test_task_search(self):
        with allure.step('Go to https://avito-tech-internship-psi.vercel.app/issues'):
            assert self.main_page.is_opened(), 'Main page should be open.'

        with allure.step('Enter in search field name of task'):
            assert self.main_page.search_task('Реализация новой галереи изображений'), 'Task was not found in the list.'
