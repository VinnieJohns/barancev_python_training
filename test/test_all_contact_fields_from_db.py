__author__ = 'VinnieJohns'
from model.contact import Contact


def test_14_all_contact_fields(app, db):
    if len(db.get_contacts_list()) == 0:
        app.contact.create(Contact(fname="pleasedeleteme"))
    contacts_from_home_page = app.contact.get_contacts_list()
    for contact in contacts_from_home_page:
        db_contact = db.get_contact_info_by_id(contact.id)
        # check last name
        assert contact.lname == db_contact.lname
        # check first name
        assert contact.fname == db_contact.fname
        # check address
        assert contact.address == db_contact.address
        # check emails
        assert contact.all_emails_from_homepage == db_contact.all_emails_from_homepage
        # check phones
        assert contact.all_phones_from_homepage == db_contact.all_phones_from_homepage
