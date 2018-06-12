from model.group import Group


class GroupHelper:
    def __init__(self, app):
        self.app = app

    def return_group_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("groups").click()

    def open_group_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("groups").click()

    def create(self, group):
        wd = self.app.wd
        # Открытие страницы создания группы
        self.open_group_page()
        # Создание новой группы
        wd.find_element_by_name("new").click()
        # Заполнение полей формы
        self.fill_group_form(group)
        # Сохранение создаваемой группы
        wd.find_element_by_name("submit").click()
        # Возвращение на страницу со списком групп
        self.return_group_page()
        self.group_cache = None

    def delete_first_group(self):
        self.delete_group_by_index(0)

    def delete_group_by_index(self, index):
        wd = self.app.wd
        # Открытие страницы создания группы
        self.open_group_page()
        # Выбор случайной группы
        self.select_first_group_by_index(index)
        # Клик по кнопке удаления
        wd.find_element_by_name("delete").click()
        # Возвращение на страницу с группами
        self.return_group_page()
        self.group_cache = None

    def select_first_group(self):
        self.select_first_group_by_index(0)

    def select_first_group_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def edit_first_group(self, group):
        wd = self.app.wd
        # Открытие страницы со списком групп
        self.open_group_page()
        # Выбор редактируемой группы
        self.select_first_group()
        # Нажатие на кнопку "Edit group"
        wd.find_element_by_name("edit").click()
        # Заполнение полей формы
        self.fill_group_form(group)
        # Нажатие на кнопку "update"
        wd.find_element_by_name("update").click()
        # Возвращение на страницу со списком групп
        self.return_group_page()
        self.group_cache = None

    def fill_group_form(self, group):
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            # Выбор и заполнение поля "Group name"
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def count(self):
        wd = self.app.wd
        self.open_group_page()
        return len(wd.find_elements_by_name("selected[]"))

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_group_page()
            # Создаем список
            self.group_cache = []
            # Получаем список элементов на странице
            for element in wd.find_elements_by_css_selector("span.group"):
                # Присваиваем текст найденного элемента переменной
                text = element.text
                # Присваиваем значение атрибута элемента переменной
                id = element.find_element_by_name("selected[]").get_attribute("value")
                # Добавляем в список найденные элементы
                self.group_cache.append(Group(name=text, id=id))
        # Возвращаем получившийся список
        return list(self.group_cache)
