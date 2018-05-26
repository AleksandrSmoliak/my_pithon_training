# -*- coding: utf-8 -*-

from contact_class import Contact
import pytest
from Application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

    
def test_test_add_contact(app):
    app.login(username="admin", password="secret")
    app.create_new_contact(Contact(firstname="Александр", middlename="Владимирович", lastname="Смоляк", nickname="Crucis",
                                title="Новый контакт", company="Новая компания", address="Адрес компании",
                                home_phone="+7(812)999-99-99", mobile_phone="+7(911)923-00-99", work_phone="+7(812)777-77-77",
                                email="crucis.spb@gmail.com", homepage="http://site.ru/",
                                option_day_birthday="//div[@id='content']/form/select[1]//option[12]",
                                option_month_birthday="//div[@id='content']/form/select[2]//option[7]", year_birthday="1983",
                                home_address="Домашний адрес"))
    app.logout()
