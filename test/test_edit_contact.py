from model.contact_class import Contact
from random import randrange

def test_edit_contact(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Александр", middlename="Владимирович", lastname="Смоляк", nickname="Crucis",
                               title="Новый контакт", company="Новая компания", address="Адрес компании",
                               home_phone="+7(812)999-99-99", mobile_phone="+7(911)923-00-99", work_phone="+7(812)777-77-77",
                               email="crucis.spb@gmail.com", homepage="http://site.ru/",
                               option_day_birthday="//div[@id='content']/form/select[1]//option[12]",
                               option_month_birthday="//div[@id='content']/form/select[2]//option[7]", year_birthday="1983",
                               home_address="Домашний адрес"))
    old_contact = db.get_contact_list()
    index = randrange(len(old_contact))
    contact = Contact(firstname="Имя", middlename="Отчество", lastname="Фамилия", nickname="Nickname",
                               title="Заголовок контакта", company="Название компании", address="Новый адрес компании",
                               home_phone="+7(812)999-99-99", mobile_phone="+7(911)923-00-99", work_phone="+7(911)999-99-99",
                               email="newmail@mail.com", homepage="http://NewSite.ru/", home_address="Редактирование Домашнего адреса")
    contact.id = old_contact[index].id
    app.contact.edit_contact_by_index(contact, index)
    new_contact = db.get_contact_list()
    assert len(old_contact) == len(new_contact)
    old_contact[index] = contact
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)

