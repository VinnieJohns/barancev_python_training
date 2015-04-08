__author__ = 'VinnieJohns'
from model.group import Group


class GroupHelper:

    # variable for storing list of groups
    groups_cache = None

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
        self.groups_cache = None

    def select_first_group(self):
        self.select_group_by_index(0)

    def select_group_by_index(self, index):
        wd = self.app.wd
        # select first group
        wd.find_elements_by_name("selected[]")[index].click()

    def modify_first_group(self, new_group_data):
        self.modify_group_by_index(0, new_group_data)

    def modify_group_by_index(self, index, new_group_data):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_index(index)
        # open group modification form
        wd.find_element_by_name("edit").click()
        self.fill_group_form(new_group_data)
        # press "submit"
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()
        self.groups_cache = None

    def delete_first_group(self):
        self.delete_group_by_index(0)

    def delete_group_by_index(self, index):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_index(index)
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()
        self.groups_cache = None

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements_by_name("selected[]"))

    def get_group_list(self):
        if self.groups_cache is None:
            wd = self.app.wd
            self.open_groups_page()
            self.groups_cache = []
            for elem in wd.find_elements_by_css_selector("span.group"):
                text = elem.text
                id = elem.find_element_by_name("selected[]").get_attribute('value')
                self.groups_cache.append(Group(name=text, id=id))
        return list(self.groups_cache)