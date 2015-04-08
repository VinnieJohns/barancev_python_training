__author__ = 'VinnieJohns'
from model.contact import Contact


def test_modify_first_contact(app):
    '''
    please note that anniversary_date_month values are lowercase letters only
    '''
    new_contact_data = Contact(fname="mod_fname0", midname="mod_mname0", lname="mod_lname0", nickname="mod_nickname",
                               title="mod_title", company="mod_ACME", address="Aptekarskaya. 99/33",
                               home_tel="305-101-2", mobile_tel="no_phone", work_tel="400-2501", fax="mod_fax",
                               email="modemail@example.com", email_2="mod@mod.com", email_3="mod_nickname@mod.org",
                               homepage="http://mod-homepage.net", birth_date_day=8, birth_date_month="March",
                               birth_date_year=1974, anniversary_date_day=18, anniversary_date_month="july",
                               anniversary_date_year=1999, secondary_address="Aptekarskaya. 99/33",
                               secondary_home_phone="modsecphone", notes="Modified notes.")
    if app.contact.count() == 0:
        app.contact.create(Contact(fname="pleasedeleteme"))
    old_contacts = app.contact.get_contacts_list()
    new_contact_data.id = old_contacts[0].id
    app.contact.modify_first_contact(new_contact_data)
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = new_contact_data
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)