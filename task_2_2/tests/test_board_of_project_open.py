import allure

from task_2_2.pages.main_page import MainPage


class TestBoardOfProjectOpen:
    main_page = MainPage()
    task_name = 'Реализация новой галереи изображений'
    task_description = 'Реализация нового UI компонента с учетом гайдлайнов дизайн-системы. Детали будут уточнены в процессе разработки'
    executor = 'Илья Романов'

    def test_board_of_project_open(self):
        with allure.step('Перейти на https://avito-tech-internship-psi.vercel.app/issues'):
            assert self.main_page.is_opened(), 'Main page should be open.'

        with allure.step('Choose on task and go to board.'):
            self.main_page.click_on_task(self.task_name)
            self.main_page.go_to_board()
            assert self.main_page.fields_match(self.task_name, self.task_description, self.executor), ''
