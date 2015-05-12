__author__ = 'VinnieJohns'
import mysql.connector
from model.group import Group
from model.contact import Contact
import re


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = mysql.connector.connect(host=host, database=name, user=user, password=password)
        self.connection.autocommit = True

    def get_group_list(self):
        group_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list;")
            for row in cursor:
                (id, name, header, footer) = row
                group_list.append(Group(id=str(id), name=str(name), header=header, footer=footer))
        finally:
            cursor.close()
        return group_list

    def get_contacts_list(self):
        contact_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, address, home, mobile, work, phone2, email, email2, email3 from addressbook where deprecated='0000-00-00 00:00:00';")
            for row in cursor:
                (id, firstname, lastname, address, home, mobile, work, phone2, email, email2, email3) = row
                contact_list.append(Contact(id=str(id), fname=firstname, lname=lastname, address=address,
                                            all_emails_from_homepage=self.merge_emails_like_on_home_page([email, email2, email3]),
                                            all_phones_from_homepage=self.merge_phones_like_on_home_page([home, mobile, work, phone2])))
        finally:
            cursor.close()
        return contact_list

    def get_contact_info_by_id(self, id):
        contact_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, address, home, mobile, work, phone2, email, email2, email3 from addressbook where id='%s';" % id)
            for row in cursor:
                (id, firstname, lastname, address, home, mobile, work, phone2, email, email2, email3) = row
                contact_list.append(Contact(id=str(id), fname=firstname, lname=lastname, address=address,
                                            all_phones_from_homepage=self.merge_phones_like_on_home_page([home, mobile, work, phone2]),
                                            all_emails_from_homepage=self.merge_emails_like_on_home_page([email, email2, email3])))
        finally:
            cursor.close()
        return contact_list[0]

    def destroy(self):
        self.connection.close()

    def clear(self, s):
        return re.sub("[() -]", "", s)

    def merge_phones_like_on_home_page(self, list):
        return "\n".join(filter(lambda x: x != "",
                                map(lambda x: self.clear(x),
                                    filter(lambda x: x is not None,
                                           list))))

    def merge_emails_like_on_home_page(self, list):
        return "\n".join(filter(lambda x: x != "",
                                filter(lambda x: x is not None,
                                       list)))