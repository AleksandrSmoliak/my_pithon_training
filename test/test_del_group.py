from model.group import Group


def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Group1", header="Group1_Header", footer="Group1_Footer"))
    old_groups = app.group.get_group_list()
    app.group.delete_first_group()
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    # Удаляем из списка первый элемент
    old_groups[0:1] = []
    # Сравниваем старый и новый списки
    assert old_groups == new_groups
