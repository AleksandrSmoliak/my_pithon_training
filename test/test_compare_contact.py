import re
from random import randrange
from model.contact_class import Contact

def test_compare_contact(app, db):
    all_contact = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    def clean(contact):
        return Contact(id=contact.id, firstname=contact.firstname.strip(), lastname=contact.lastname.strip(),
                middlename=contact.middlename.strip(), nickname=contact.nickname.strip(), title=contact.title.strip(),
                company=contact.company.strip(), address=contact.address.strip(), home_phone=contact.home_phone.strip(),
                mobile_phone=contact.mobile_phone.strip(), work_phone=contact.work_phone.strip(), email=contact.email.strip(),
                homepage=contact.homepage.strip())
    # Получаем список контактов из БД и очищаем от пробелов
    contacts_db = sorted(map(clean, db.get_contact_list()), key=Contact.id_or_max)
    # Получаем значения полей контакта со сгенерированным индексом с главной страницы
    contact_from_home_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)

    for index in range(0, len(all_contact)-1):
        assert contact_from_home_page[index].firstname == contacts_db[index].firstname
        assert contact_from_home_page[index].lastname == contacts_db[index].lastname
        assert contact_from_home_page[index].address == contacts_db[index].address
        assert contact_from_home_page[index].all_phones_from_home_page == merge_phones_like_on_home_page(contacts_db[index])
        assert contact_from_home_page[index].all_email_from_home_page == merge_email_like_on_home_page(contacts_db[index])

def merge_email_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear_space(clear_mail(x)),
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3]))))

def clear_space(s):
    return re.sub("\s+", " ", s)

def clear_mail(s):
    return re.sub("[() -]", " ", s)

def clear_phones(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear_phones(x),
                                filter(lambda x: x is not None,
                                       [contact.home_phone, contact.mobile_phone, contact.work_phone]))))
