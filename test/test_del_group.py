from model.group import Group
from random import randrange
import random


def test_delete_some_group(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="Group1", header="Group1_Header", footer="Group1_Footer"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.delete_group_by_id(group.id)
    new_groups = db.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    # Удаляем из списка случайный элемент
    old_groups.remove(group)
    # Сравниваем старый и новый списки
    assert old_groups == new_groups
