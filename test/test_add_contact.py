# -*- coding: utf-8 -*-
from model.contact import Contact
from fixture import support
import pytest
import random

testdata = [
    Contact(fname=random.choice(["", support.random_string("fname", 10)]),
            midname=random.choice(["", support.random_string("mname", 15)]),
            lname=random.choice(["", support.random_string("lname", 20)]),
            nickname=random.choice(["", support.random_string("nickname", 10)]),
            title=random.choice(["", support.random_string("title", 10)]),
            company=random.choice(["", support.random_string("company", 25)]),
            address=random.choice(["", support.random_string("address", 30)]),
            home_tel=random.choice(["", support.random_string("home_tel", 10)]),
            mobile_tel=random.choice(["", support.random_string("mobile_tel", 10)]),
            work_tel=random.choice(["", support.random_string("work_tel", 10)]),
            fax=random.choice(["", support.random_string("fax", 10)]),
            email_2=random.choice(["", support.random_string("email2", 10)]),
            email_3=random.choice(["", support.random_string("email3", 10)]),
            homepage=random.choice(["", support.random_string("homepage", 10)]),
            birth_date_day=random.randrange(0, 32),
            birth_date_month=random.choice(["-", random.choice(support.months_list)]),
            birth_date_year=random.choice(["", random.randrange(1898, 2015)]),
            anniversary_date_day=random.randrange(0, 32),
            anniversary_date_month=random.choice(["-", random.choice(support.months_list)]),
            anniversary_date_year=random.choice(["", random.randrange(1898, 2015)]),
            secondary_address=random.choice(["", support.random_string("secaddress", 30)]),
            secondary_home_phone=random.choice(["", support.random_string("phone2", 10)]),
            notes=random.choice(["", support.random_string("notes", 100)]))
    for i in range(5)
    ] + [Contact(fname="", lname="")]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contacts_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contacts_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)