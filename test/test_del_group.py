from model.group import Group
from random import randrange


def test_delete_some_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Group1", header="Group1_Header", footer="Group1_Footer"))
    old_groups = app.group.get_group_list()
    # Вычисляем случайную группу из списка
    index = randrange(len(old_groups))
    app.group.delete_group_by_index(index)
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    # Удаляем из списка случайный элемент
    old_groups[index:index+1] = []
    # Сравниваем старый и новый списки
    assert old_groups == new_groups
