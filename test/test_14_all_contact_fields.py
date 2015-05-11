__author__ = 'VinnieJohns'
from model.contact import Contact
from random import randrange
import re


def test_14_all_contact_fields(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(fname="pleasedeleteme"))
    contacts = app.contact.get_contacts_list()
    index = randrange(len(contacts))
    contact_from_home_page = contacts[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    # check last name
    assert contact_from_home_page.lname == contact_from_edit_page.lname
    # check first name
    assert contact_from_home_page.fname == contact_from_edit_page.fname
    # check address
    assert contact_from_home_page.address == contact_from_edit_page.address
    # check emails
    assert contact_from_home_page.all_emails_from_homepage == merge_emails_like_on_home_page(contact_from_edit_page)
    # check phones
    assert contact_from_home_page.all_phones_from_homepage == merge_phones_like_on_home_page(contact_from_edit_page)


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home_tel, contact.mobile_tel,
                                        contact.work_tel, contact.secondary_home_phone]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email_2, contact.email_3]))))
