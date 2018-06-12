from model.contact_class import Contact


def test_delete_first_contact(app):
    if app.contact.contact_count() == 0:
        app.contact.create(Contact(firstname="Александр", middlename="Владимирович", lastname="Смоляк", nickname="Crucis",
                               title="Новый контакт", company="Новая компания", address="Адрес компании",
                               home_phone="+7(812)999-99-99", mobile_phone="+7(911)923-00-99", work_phone="+7(812)777-77-77",
                               email="crucis.spb@gmail.com", homepage="http://site.ru/",
                               option_day_birthday="//div[@id='content']/form/select[1]//option[12]",
                               option_month_birthday="//div[@id='content']/form/select[2]//option[7]", year_birthday="1983",
                               home_address="Домашний адрес"))
    old_contact = app.contact.get_contact_list()
    app.contact.delete_first_contact()
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) - 1 == len(new_contact)
