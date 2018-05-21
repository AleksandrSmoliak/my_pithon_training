# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest
from contact_class import Contact


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


class test_add_contact(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver(capabilities={"marionette": False})
        self.wd.implicitly_wait(60)
    
    def test_test_add_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.create_new_contact(wd, Contact(firstname="Александр", middlename="Владимирович", lastname="Смоляк", nickname="Crucis",
                                title="Новый контакт", company="Новая компания", address="Адрес компании",
                                home_phone="+7(812)999-99-99", mobile_phone="+7(911)923-00-99", work_phone="+7(812)777-77-77",
                                email="crucis.spb@gmail.com", homepage="http://site.ru/",
                                option_day_birthday="//div[@id='content']/form/select[1]//option[12]",
                                option_month_birthday="//div[@id='content']/form/select[2]//option[7]", year_birthday="1983",
                                home_address="Домашний адрес"))
        self.logout(wd)

    def logout(self, wd):
        # Логаут
        wd.find_element_by_link_text("Logout").click()

    def create_new_contact(self, wd, Contact):
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

    def login(self, wd, username, password):
        # Авторизация
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def open_home_page(self, wd):
        # Открытие домашней страницы
        wd.get("http://localhost/addressbook/")

    def tearDown(self):
        self.wd.quit()


if __name__ == '__main__':
    unittest.main()
