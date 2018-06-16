# -*- coding: utf-8 -*-

from model.contact_class import Contact
import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", middlename="", lastname="", nickname="",
                               title="", company="", address="",
                               home_phone="", mobile_phone="", work_phone="",
                               email="", homepage="",
                               option_day_birthday="",
                               option_month_birthday="", year_birthday="",
                               home_address="")] + [
            Contact(firstname=random_string("firstname", 10),
                    middlename=random_string("middlename", 10), lastname=random_string("lastname", 10),
                    nickname=random_string("nickname", 10), title=random_string("title", 10),
                    company=random_string("company", 10), address=random_string("address", 10),
                    home_phone=random_string("home_phone", 10), mobile_phone=random_string("mobile_phone", 10),
                    work_phone=random_string("work_phone", 10), email=random_string("email", 10),
                    homepage=random_string("homepage", 10), option_day_birthday="//div[@id='content']/form/select[1]//option[12]",
                    option_month_birthday="//div[@id='content']/form/select[2]//option[7]",
                    year_birthday=random_string("year_birthday", 10), home_address=random_string("home_address", 10))
    for i in range(5)
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_test_add_contact(app, contact):
    old_contact = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contact) + 1 == app.contact.contact_count()
    new_contact = app.contact.get_contact_list()
    old_contact.append(contact)
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)
