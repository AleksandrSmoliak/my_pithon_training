from model.group import Group


def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Group1", header="Group1_Header", footer="Group1_Footer"))
    app.group.delete_first_group()
