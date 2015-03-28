__author__ = 'VinnieJohns'


class SessionHelper:


    def __init__(self, app):
        self.app = app

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def login(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
        self.change_field_value("user", username)
        self.change_field_value("pass", password)
        wd.find_element_by_css_selector("input[type=\"submit\"]").click()

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()