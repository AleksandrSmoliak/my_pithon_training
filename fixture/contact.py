class ContactHelper:
    def __init__(self, app):
        self.app = app

    def create(self, Contact):
        wd = self.app.wd
        # Добавление нового контакта
        wd.find_element_by_link_text("add new").click()
        # Заполнение поля "Имя"
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(Contact.firstname)
        # Заполнение поля "Отчество"
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(Contact.middlename)
        # Заполнение поля "Фамилия"
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(Contact.lastname)
        # Заполнение поля "Псевдоним"
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(Contact.nickname)
        # Заполнение поля "Заголовок"
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(Contact.title)
        # Заполнение поля "Компания"
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(Contact.company)
        # Заполнение поля "Адрес компании"
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(Contact.address)
        # Заполнение поля "Домашний телефон"
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(Contact.home_phone)
        # Заполнение поля "Мобильный телефон"
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(Contact.mobile_phone)
        # Заполнение поля "Рабочий телефон"
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(Contact.work_phone)
        # Заполнение поля "E-mail"
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(Contact.email)
        # Заполнение поля "Домашняя страница"
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(Contact.homepage)
        # Выбор дня даты рождения (выпадающий список)
        if not wd.find_element_by_xpath(Contact.option_day_birthday).is_selected():
            wd.find_element_by_xpath(Contact.option_day_birthday).click()
        # Выбор месяца даты рождения (выпадающий список)
        if not wd.find_element_by_xpath(Contact.option_month_birthday).is_selected():
            wd.find_element_by_xpath(Contact.option_month_birthday).click()
        # Заполнение поля "Год рождения"
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(Contact.year_birthday)
        # Заполнение поля "Домашний адрес"
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(Contact.home_address)
        # Сохранение контакта
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def delete_first_contact(self):
        wd = self.app.wd
        # Выбор контакта
        wd.find_element_by_name("selected[]").click()
        # Клик по кнопке удаления
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()

    def edit_first_contact(self, Contact):
        wd = self.app.wd
        # Нажатие кнопки "Edit" для редактирования
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        # Заполнение поля "Имя"
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(Contact.firstname)
        # Заполнение поля "Отчество"
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(Contact.middlename)
        # Заполнение поля "Фамилия"
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(Contact.lastname)
        # Заполнение поля "Псевдоним"
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(Contact.nickname)
        # Заполнение поля "Заголовок"
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(Contact.title)
        # Заполнение поля "Компания"
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(Contact.company)
        # Заполнение поля "Адрес компании"
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(Contact.address)
        # Заполнение поля "Домашний телефон"
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(Contact.home_phone)
        # Заполнение поля "Мобильный телефон"
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(Contact.mobile_phone)
        # Заполнение поля "Рабочий телефон"
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(Contact.work_phone)
        # Заполнение поля "E-mail"
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(Contact.email)
        # Заполнение поля "Домашняя страница"
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(Contact.homepage)
        # Выбор дня даты рождения (выпадающий список)
        if not wd.find_element_by_xpath(Contact.option_day_birthday).is_selected():
            wd.find_element_by_xpath(Contact.option_day_birthday).click()
        # Выбор месяца даты рождения (выпадающий список)
        if not wd.find_element_by_xpath(Contact.option_month_birthday).is_selected():
            wd.find_element_by_xpath(Contact.option_month_birthday).click()
        # Заполнение поля "Год рождения"
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(Contact.year_birthday)
        # Заполнение поля "Домашний адрес"
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(Contact.home_address)
        # Нажатие кнопки "Update"
        wd.find_element_by_name("update").click()
