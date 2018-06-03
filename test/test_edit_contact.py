from model.contact_class import Contact


def test_edit_contact(app):
    app.contact.edit_first_contact(Contact(firstname="Имя", middlename="Отчество", lastname="Фамилия", nickname="Nickname",
                               title="Заголовок контакта", company="Название компании", address="Новый адрес компании",
                               home_phone="+7(812)999-99-99", mobile_phone="+7(911)923-00-99", work_phone="+7(911)999-99-99",
                               email="newmail@mail.com", homepage="http://NewSite.ru/",
                               option_day_birthday="//div[@id='content']/form/select[1]//option[12]",
                               option_month_birthday="//div[@id='content']/form/select[2]//option[7]", year_birthday="1999",
                               home_address="Редактирование Домашнего адреса"))
