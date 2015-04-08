__author__ = 'VinnieJohns'
from model.group import Group
from random import randrange


def test_modify_random_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="pleaseModifyMeme"))
    old_groups = app.group.get_group_list()
    group = Group(name="mod_name03", header="mod_header13", footer="mod_footer23")
    index = randrange(len(old_groups))
    group.id = old_groups[index].id
    app.group.modify_group_by_index(index, group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)