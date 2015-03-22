# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    new_contact = Contact(fname="fname", midname="mname", lname="lname", nickname="nickname",
                          title="title", company="ACME LTD", address="Synyavinskaya st. 12/3", home_tel="100-500-1",
                          mobile_tel="+7(999) 100-500-2", work_tel="200-1000", fax="fax", email="",
                          email_2="lname@company.com", email_3="nickname@example.org", homepage="http://homepage.net",
                          birth_date_day=12, birth_date_month="March", birth_date_year=1987,
                          anniversary_date_day=23, anniversary_date_month="April", anniversary_date_year=2014,
                          secondary_address="Synyavinskaya st. 3/12", secondary_home_phone="200-500-1",
                          notes="Here should be some notes. Someday.")
    app.session.login(username="admin", password="secret")
    app.contact.create(new_contact)
    app.session.logout()
