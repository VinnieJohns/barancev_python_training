__author__ = 'VinnieJohns'
from model.group import Group


def test_modify_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="pleaseModifyMeme"))
    old_groups = app.group.get_group_list()
    group = Group(name="mod_name03", header="mod_header13", footer="mod_footer23")
    group.id = old_groups[0].id
    app.group.modify_first_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)