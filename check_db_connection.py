__author__ = 'VinnieJohns'
from fixture.db import DbFixture

db = DbFixture(host="127.0.0.1", name="addressbook", user="root", password="")

try:
    contacts = db.get_contacts_list()
    for contact in contacts:
        print contact, contact.all_emails_from_homepage, contact.all_phones_from_homepage
    print len(contacts)
    print db.get_contact_info_by_id(114)
finally:
    db.destroy()