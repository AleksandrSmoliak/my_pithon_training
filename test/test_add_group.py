# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    # Получаем текущий список групп
    old_groups = app.group.get_group_list()
    # В локальную переменную добавляем группу
    group = Group(name="Group1", header="Group1_Header", footer="Group1_Footer")
    # Добавляем новую группу
    app.group.create(group)
    # Получаем новый список групп
    new_groups = app.group.get_group_list()
    # Сравниваем длинну старого списка групп с новым
    assert len(old_groups) + 1 == len(new_groups)
    # В переменную добавляем ту же самую группу, что добавили через интерфейс
    old_groups.append(group)
    # Проверка сравнения старой и новой группы
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_add_group_empty(app):
    # Получаем текущий список групп
    old_groups = app.group.get_group_list()
    # В локальную переменную добавляем группу
    group = Group(name="", header="", footer="")
    # Добавляем новую пустую группу
    app.group.create(group)
    # Получаем новый список групп
    new_groups = app.group.get_group_list()
    # Сравниваем длинну старого списка групп с новым
    assert len(old_groups) + 1 == len(new_groups)
    # В переменную добавляем ту же самую группу, что добавили через интерфейс
    old_groups.append(group)
    # Проверка сравнения старой и новой группы
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
