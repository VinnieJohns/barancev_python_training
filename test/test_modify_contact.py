__author__ = 'VinnieJohns'
from model.contact import Contact
import random


def test_modify_random_contact(app, db, check_ui):
    # please note that anniversary_date_month values are lowercase letters only
    new_contact_data = Contact(fname="mod_fname0", midname="mod_mname0", lname="mod_lname0", nickname="mod_nickname",
                               title="mod_title", company="mod_ACME", address="Aptekarskaya. 99/33",
                               home_tel="305-101-2", mobile_tel="no_phone", work_tel="400-2501", fax="mod_fax",
                               email="modemail@example.com", email_2="mod@mod.com", email_3="mod_nickname@mod.org",
                               homepage="http://mod-homepage.net", birth_date_day=8, birth_date_month="March",
                               birth_date_year=1974, anniversary_date_day=18, anniversary_date_month="july",
                               anniversary_date_year=1999, secondary_address="Aptekarskaya. 99/33",
                               secondary_home_phone="modsecphone", notes="Modified notes.")
    if len(db.get_contacts_list()) == 0:
        app.contact.create(Contact(fname="pleasedeleteme"))
    old_contacts = db.get_contacts_list()
    contact = random.choice(old_contacts)
    new_contact_data.id = contact.id
    index = old_contacts.index(contact)
    app.contact.modify_contact_by_id(contact.id, new_contact_data)
    new_contacts = db.get_contacts_list()
    old_contacts[index] = new_contact_data
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contacts_list(), key=Contact.id_or_max)