from model.contact_class import Contact
import re

class ContactHelper:
    def __init__(self, app):
        self.app = app

    def create(self, Contact):
        wd = self.app.wd
        # Открытие домашней страницы
        self.app.open_home_page()
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
        self.app.open_home_page()
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        # Открытие домашней страницы
        self.app.open_home_page()
        # Выбор контакта
        wd.find_elements_by_name("selected[]")[index].click()
        # Клик по кнопке удаления
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        # Открытие домашней страницы
        self.app.open_home_page()
        # Выбор контакта
        self.select_contact_by_id(id)
        # Клик по кнопке удаления
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def remove_contact_from_group(self, id_group, id_contact):
        wd = self.app.wd
        # Переходим на страницу с контактами
        self.app.open_home_page()
        # Фильтруем контакты по группе
        self.filter_group_by_id(id_group)
        # Выбираем случайную группу по ИД
        self.select_contact_by_id(id_contact)
        # Удаляем выбранный контакт из группы
        wd.find_element_by_xpath("//input[@name='remove']").click()


    def edit_first_contact(self, Contact):
        self.edit_contact_by_index(Contact, 0)

    def filter_group_by_id(self, id):
        wd = self.app.wd
        # Выбираем в фильтре группу по id
        wd.find_element_by_xpath("//select[@name='group']//option[@value='%s']" % id).click()

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value = '%s']" % id).click()

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        # Открытие домашней страницы
        self.app.open_home_page()
        # Нажатие кнопки "Edit" для редактирования
        wd.find_elements_by_xpath("//table[@id='maintable']/tbody/tr[@name='entry']/td[8]/a/img")[index].click()

    def edit_contact_by_index(self, Contact, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
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
        # Заполнение поля "Домашний адрес"
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(Contact.home_address)
        # Нажатие кнопки "Update"
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def contact_count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                cells = element.find_elements_by_tag_name("td")
                firstname = cells[2].text
                lastname = cells[1].text
                address = cells[3].text
                allemail = cells[4].text
                id = cells[0].find_element_by_name("selected[]").get_attribute("value")
                all_phones = cells[5].text
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, address=address, all_email_from_home_page=allemail,
                                                  id=id, all_phones_from_home_page=all_phones))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        address = wd.find_element_by_name("address").text
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        home_phone = wd.find_element_by_name("home").get_attribute("value")
        mobile_phone = wd.find_element_by_name("mobile").get_attribute("value")
        work_phone = wd.find_element_by_name("work").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, address=address, email=email, email2=email2, email3=email3,
                       id=id, home_phone=home_phone, mobile_phone=mobile_phone, work_phone=work_phone)

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        home_phone = re.search("H: (.*)", text).group(1)
        mobile_phone = re.search("M: (.*)", text).group(1)
        work_phone = re.search("W: (.*)", text).group(1)
        return Contact(home_phone=home_phone, mobile_phone=mobile_phone, work_phone=work_phone)