__author__ = 'VinnieJohns'
from model.group import Group


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("groups").click()

    def fill_group_form(self, group):
        self.app.session.change_field_value("group_name", group.name)
        self.app.session.change_field_value("group_header", group.header)
        self.app.session.change_field_value("group_footer", group.footer)

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # press "new"
        wd.find_element_by_name("new").click()
        self.fill_group_form(group)
        # press "submit"
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def select_first_group(self):
        wd = self.app.wd
        # select first group
        wd.find_element_by_name("selected[]").click()

    def modify_first_group(self, new_group_data):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        # open group modification form
        wd.find_element_by_name("edit").click()
        self.fill_group_form(new_group_data)
        # press "submit"
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()

    def delete_first_group(self):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()


    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements_by_name("selected[]"))

    def get_group_list(self):
        wd = self.app.wd
        self.open_groups_page()
        groups = []
        for elem in wd.find_elements_by_css_selector("span.group"):
            text = elem.text
            id = elem.find_element_by_name("selected[]").get_attribute('value')
            groups.append(Group(name=text, id=id))
        return groups