# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    '''
    email is auto-generated, don't pass it at all to check it
    '''
    new_contact = Contact(fname="fname", midname="mname", lname="lname", nickname="nickname", title="title",
                          company="ACME LTD", address="Synyavinskaya st. 12/3", home_tel="100-500-1",
                          mobile_tel="+7(999) 100-500-2", work_tel="200-1000", fax="fax",
                          email_2="lname@company.com", email_3="nickname@example.org", homepage="http://homepage.net",
                          birth_date_day=12, birth_date_month="March", birth_date_year=1987, anniversary_date_day=23,
                          anniversary_date_month="April", anniversary_date_year=2014,
                          secondary_address="Synyavinskaya st. 3/12", secondary_home_phone="200-500-1",
                          notes="Here should be some notes. Someday.")
    old_contacts = app.contact.get_contacts_list()
    app.contact.create(new_contact)
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(new_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)