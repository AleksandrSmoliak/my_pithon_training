# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app, json_groups):
    group = json_groups
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