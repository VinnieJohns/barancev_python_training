__author__ = 'VinnieJohns'
from model.contact import Contact
import re


class ContactHelper:

    # variable for storing list of groups
    contacts_cache = None

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
        self.contacts_cache = None

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.open_home_page_by_nav()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.open_home_page_by_nav()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        fname = wd.find_element_by_name("firstname").get_attribute("value")
        lname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        home_tel = wd.find_element_by_name("home").get_attribute("value")
        mobile_tel = wd.find_element_by_name("mobile").get_attribute("value")
        work_tel = wd.find_element_by_name("work").get_attribute("value")
        secondary_home_phone = wd.find_element_by_name("phone2").get_attribute("value")
        # getting additional fields for 14-th task
        midname = wd.find_element_by_name("middlename").get_attribute("value")
        nickname = wd.find_element_by_name("nickname").get_attribute("value")
        title = wd.find_element_by_name("title").get_attribute("value")
        company = wd.find_element_by_name("company").get_attribute("value")
        address = wd.find_element_by_name("address").text
        fax = wd.find_element_by_name("fax").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email_2 = wd.find_element_by_name("email2").get_attribute("value")
        email_3 = wd.find_element_by_name("email3").get_attribute("value")
        homepage = wd.find_element_by_name("homepage").get_attribute("value")
        secondary_address = wd.find_element_by_name("address2").text
        notes = wd.find_element_by_name("notes").text
        # it's still an open question for birth_date_day, birth_date_month, birth_date_year
        # and for anniversary_date_day, anniversary_date_month, anniversary_date_year
        return Contact(fname=fname, lname=lname, id=id, home_tel=home_tel,
                       mobile_tel=mobile_tel, work_tel=work_tel, fax=fax,
                       secondary_home_phone=secondary_home_phone, title=title,
                       midname=midname, nickname=nickname, company=company,
                       address=address, email=email, email_2=email_2, email_3=email_3,
                       homepage=homepage, secondary_address=secondary_address, notes=notes)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        home_tel = re.search("H: (.*)", text).group(1)
        mobile_tel = re.search("M: (.*)", text).group(1)
        work_tel = re.search("W: (.*)", text).group(1)
        secondary_home_phone = re.search("P: (.*)", text).group(1)
        return Contact(home_tel=home_tel, mobile_tel=mobile_tel,
                       work_tel=work_tel, secondary_home_phone=secondary_home_phone)

    def modify_first_contact(self, new_contact_data):
        self.modify_contact_by_index(0, new_contact_data)

    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.open_home_page_by_nav()
        wd.find_elements_by_css_selector("img[title='Edit']")[index].click()
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_css_selector("div[id='content'] form input[name='update']").click()
        self.open_home_page_by_nav()
        self.contacts_cache = None

    def modify_contact_by_id(self, id, new_contact_data):
        wd = self.app.wd
        self.open_home_page_by_nav()
        wd.find_element_by_css_selector("a[href='edit.php?id=%s']" % id).click()
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_css_selector("div[id='content'] form input[name='update']").click()
        self.open_home_page_by_nav()
        self.contacts_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_home_page_by_nav()
        # select first contact
        wd.find_elements_by_name("selected[]")[index].click()
        # submit deletion
        wd.find_element_by_css_selector("input[value='Delete']").click()
        wd.switch_to_alert().accept()
        self.open_home_page_by_nav()
        self.contacts_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.open_home_page_by_nav()
        # select first contact
        wd.find_element_by_id(id).click()
        # submit deletion
        wd.find_element_by_css_selector("input[value='Delete']").click()
        wd.switch_to_alert().accept()
        self.open_home_page_by_nav()
        self.contacts_cache = None

    def open_home_page_by_nav(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/")):
            wd.find_element_by_link_text("home").click()

    def count(self):
        wd = self.app.wd
        self.open_home_page_by_nav()
        return len(wd.find_elements_by_name("selected[]"))

    def get_contacts_list(self):
        if self.contacts_cache is None:
            wd = self.app.wd
            self.open_home_page_by_nav()
            self.contacts_cache = []
            for elem in wd.find_elements_by_name("entry"):
                id = elem.find_element_by_name("selected[]").get_attribute('id')
                lname = elem.find_elements_by_css_selector("td")[1].text
                fname = elem.find_elements_by_css_selector("td")[2].text
                address = elem.find_elements_by_css_selector("td")[3].text
                all_emails = elem.find_elements_by_css_selector("td")[4].text
                all_phones = elem.find_elements_by_css_selector("td")[5].text
                self.contacts_cache.append(Contact(fname=fname, lname=lname, id=str(id), address=address,
                                                   all_emails_from_homepage=all_emails,
                                                   all_phones_from_homepage=all_phones))
        return list(self.contacts_cache)