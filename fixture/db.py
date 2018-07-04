import pymysql.cursors
import mysql.connector
from model.group import Group
from model.contact_class import Contact


class DbFixture:
    def __init__(self, host, name, user, password):
        self.host = host,
        self.name = name,
        self.user = user,
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password)
        # Сбрасывает кеш БД (позволяет получить реальные данные из БД, без искажения)
        self.connection.autocommit(True)

    def get_group_list(self):
        list=[]
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list=[]
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, middlename, nickname, title, company, address, home, mobile,"
                           "work, email, homepage from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname, middlename, nickname, title, company, address, home, mobile, work, email,
                 homepage) = row
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname, middlename=middlename, nickname=nickname,
                title=title, company=company, address=address, home_phone=home, mobile_phone=mobile, work_phone=work,
                email=email, homepage=homepage))
        finally:
            cursor.close()
        return list

    def get_group_with_contact_list(self):
        list=[]
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id from address_in_groups")
            for row in cursor:
                (id,) = row
                list.append(Group(id=str(id)))
        finally:
            cursor.close()
        return list


    def destroy(self):
        self.connection.close()