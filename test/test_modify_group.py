__author__ = 'VinnieJohns'
from model.group import Group
import random


def test_modify_random_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="pleaseModifyMeme"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    new_group = Group(id=group.id, name="mod_name05", header="mod_header153", footer="mod_footer523")
    app.group.modify_group_by_id(group.id, new_group)
    new_groups = db.get_group_list()
    index = old_groups.index(group)
    old_groups[index] = new_group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)