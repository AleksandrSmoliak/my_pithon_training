import re
from random import randrange
from model.contact_class import Contact

def test_compare_contact(app, db):
    all_contact = app.contact.get_contact_list()
    def clean(contact):
        return Contact(id=contact.id, firstname=contact.firstname.strip(), lastname=contact.lastname.strip(),
                middlename=contact.middlename.strip(), nickname=contact.nickname.strip(), title=contact.title.strip(),
                company=contact.company.strip(), address=contact.address.strip(), home_phone=contact.home_phone.strip(),
                mobile_phone=contact.mobile_phone.strip(), work_phone=contact.work_phone.strip(), email=contact.email.strip(),
                homepage=contact.homepage.strip())
    # Получаем список контактов из БД и очищаем от пробелов
    contacts_db = map(clean, db.get_contact_list())
    # генерируем случайное значение с ограничением в длинну списка контактов
    index = randrange(len(all_contact))
    # Получаем значения полей контакта со сгенерированным индексом с главной страницы
    contact_from_home_page = app.contact.get_contact_list()[index]
    # Получаем значения полей контакта со сгенерированным индексом со страницы редактирования
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    # Сравниваем полный список контактов на главной странице с аналогичным списком из БД
    assert sorted(all_contact, key=Contact.id_or_max) == sorted(contacts_db, key=Contact.id_or_max)
    # Сравниваем значения полей главной страницы с полями на странице редактирования
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_email_from_home_page == merge_email_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)


def merge_email_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3])))

def clear(s):
    return re.sub("[()-]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home_phone, contact.mobile_phone, contact.work_phone]))))
