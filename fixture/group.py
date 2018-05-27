class GroupHelper:
    def __init__(self, app):
        self.app = app

    def return_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def open_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def create(self, group):
        wd = self.app.wd
        # Открытие страницы создания группы
        self.open_group_page()
        # Создание новой группы
        wd.find_element_by_name("new").click()
        # Заполнение полей группы
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # Сохранение создаваемой группы
        wd.find_element_by_name("submit").click()
        # Возвращение на страницу со списком групп
        self.return_group_page()

    def delete_first_group(self):
        wd = self.app.wd
        # Открытие страницы создания группы
        self.open_group_page()
        # Выбор группы
        wd.find_element_by_name("selected[]").click()
        # Клик по кнопке удаления
        wd.find_element_by_name("delete").click()
        # Возвращение на страницу с группами
        self.return_group_page()