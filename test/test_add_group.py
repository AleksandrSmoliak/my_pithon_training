# -*- coding: utf-8 -*-
from model.group import Group
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Group(name="", header="", footer="")] + [
    Group(name=random_string("name", 10), header=random_string("header", 20), footer=random_string("footer", 20))
    for i in range(5)
]


@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_add_group(app, group):
    pass
    # Получаем текущий список групп
    old_groups = app.group.get_group_list()
    # Добавляем новую группу
    app.group.create(group)
    # Сравниваем длинну старого списка групп с новым
    assert len(old_groups) + 1 == app.group.count()
    # Получаем новый список групп
    new_groups = app.group.get_group_list()
    # В переменную добавляем ту же самую группу, что добавили через интерфейс
    old_groups.append(group)
    # Проверка сравнения старой и новой группы
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)