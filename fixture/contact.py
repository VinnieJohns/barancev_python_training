__author__ = 'VinnieJohns'
from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_add_new_contact_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/edit.php") and len(wd.find_elements_by_name("submit")) > 0):
            wd.find_element_by_link_text("add new").click()

    def select_value_from_dropdown(self, dropdown_name, value):
        wd = self.app.wd
        if value is not None:
            wd.find_element_by_css_selector(
            "select[name='" + str(dropdown_name) + "'] option[value='" + str(value) + "']").click()

    def fill_contact_form(self, contact):
        self.app.session.change_field_value("firstname", contact.fname)
        self.app.session.change_field_value("middlename", contact.midname)
        self.app.session.change_field_value("lastname", contact.lname)
        self.app.session.change_field_value("nickname", contact.nickname)
        self.app.session.change_field_value("title", contact.title)
        self.app.session.change_field_value("company", contact.company)
        self.app.session.change_field_value("address", contact.address)
        self.app.session.change_field_value("home", contact.home_tel)
        self.app.session.change_field_value("mobile", contact.mobile_tel)
        self.app.session.change_field_value("work", contact.work_tel)
        self.app.session.change_field_value("fax", contact.fax)
        self.app.session.change_field_value("email", contact.email)
        self.app.session.change_field_value("email2", contact.email_2)
        self.app.session.change_field_value("email3", contact.email_3)
        self.app.session.change_field_value("homepage", contact.homepage)
        self.select_value_from_dropdown("bday", contact.birth_date_day)
        self.select_value_from_dropdown("bmonth", contact.birth_date_month)
        self.app.session.change_field_value("byear", contact.birth_date_year)
        self.select_value_from_dropdown("aday", contact.anniversary_date_day)
        self.select_value_from_dropdown("amonth", contact.anniversary_date_month)
        self.app.session.change_field_value("ayear", contact.anniversary_date_year)
        self.app.session.change_field_value("address2", contact.secondary_address)
        self.app.session.change_field_value("phone2", contact.secondary_home_phone)
        self.app.session.change_field_value("notes", contact.notes)

    def create(self, contact):
        wd = self.app.wd
        self.open_add_new_contact_page()
        wd.find_element_by_name("theform").click()
        self.fill_contact_form(contact)
        wd.find_element_by_css_selector("div[id='content'] form input[name='submit']").click()
        self.open_home_page_by_nav()

    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.open_home_page_by_nav()
        wd.find_element_by_css_selector("img[title='Edit']").click()
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_css_selector("div[id='content'] form input[name='update']").click()
        self.open_home_page_by_nav()

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_home_page_by_nav()
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_css_selector("input[value='Delete']").click()
        wd.switch_to_alert().accept()
        self.open_home_page_by_nav()

    def open_home_page_by_nav(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/")):
            wd.find_element_by_link_text("home").click()

    def count(self):
        wd = self.app.wd
        self.open_home_page_by_nav()
        return len(wd.find_elements_by_name("selected[]"))

    def get_contacts_list(self):
        wd = self.app.wd
        self.open_home_page_by_nav()
        contacts = []
        for elem in wd.find_elements_by_name("entry"):
            lname = elem.find_elements_by_css_selector("td")[1].text
            fname = elem.find_elements_by_css_selector("td")[2].text
            id = elem.find_element_by_name("selected[]").get_attribute('id')
            contacts.append(Contact(fname=fname, lname=lname, id=id))
        return contacts