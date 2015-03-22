__author__ = 'VinnieJohns'
from model.group import Group

def test_modify_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(name="mod_name", header="mod_header", footer="mod_footer"))
    app.session.logout()