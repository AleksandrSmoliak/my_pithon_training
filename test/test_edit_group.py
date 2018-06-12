from model.group import Group


def test_edit_first_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Group1", header="Group1_Header", footer="Group1_Footer"))
    old_groups = app.group.get_group_list()
    app.group.edit_first_group(Group(name="Edit_name"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_edit_first_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Group1", header="Group1_Header", footer="Group1_Footer"))
    old_groups = app.group.get_group_list()
    app.group.edit_first_group(Group(header="Edit_Header"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_edit_first_group_footer(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Group1", header="Group1_Header", footer="Group1_Footer"))
    old_groups = app.group.get_group_list()
    app.group.edit_first_group(Group(footer="Edit_Footer"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)