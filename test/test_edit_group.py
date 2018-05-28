from model.group import Group


def test_edit_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="Edit_name", header="Edit_Header", footer="Edit_Footer"))
    app.session.logout()