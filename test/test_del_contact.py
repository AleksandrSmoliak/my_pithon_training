from model.contact_class import Contact
from random import randrange
import time
import random

def test_delete_first_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Александр", middlename="Владимирович", lastname="Смоляк", nickname="Crucis",
                               title="Новый контакт", company="Новая компания", address="Адрес компании",
                               home_phone="+7(812)999-99-99", mobile_phone="+7(911)923-00-99", work_phone="+7(812)777-77-77",
                               email="crucis.spb@gmail.com", homepage="http://site.ru/",
                               option_day_birthday="//div[@id='content']/form/select[1]//option[12]",
                               option_month_birthday="//div[@id='content']/form/select[2]//option[7]", year_birthday="1983",
                               home_address="Домашний адрес"))
    old_contact = db.get_contact_list()
    contact = random.choice(old_contact)
    app.contact.delete_contact_by_id(contact.id)
    # Задержка в 1 секунду (связано с тем что данные не успевают удалится из базы)
    time.sleep(1)
    new_contact = db.get_contact_list()
    assert len(old_contact) - 1 == len(new_contact)
    # Удаляем из списка случайный элемент
    old_contact.remove(contact)
    # Сравниваем старый и новый списки
    assert old_contact == new_contact
    if check_ui:
        assert sorted(new_contact, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)

