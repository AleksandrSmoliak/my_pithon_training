# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    # Получаем текущий список групп
    old_groups = app.group.get_group_list()
    # Добавляем новую группу
    app.group.create(Group(name="Group1", header="Group1_Header", footer="Group1_Footer"))
    # Получаем новый список групп
    new_groups = app.group.get_group_list()
    # Сравниваем длинну старого списка групп с новым
    assert len(old_groups) + 1 == len(new_groups)


def test_add_group_empty(app):
    # Получаем текущий список групп
    old_groups = app.group.get_group_list()
    # Добавляем новую пустую группу
    app.group.create(Group(name="", header="", footer=""))
    # Получаем новый список групп
    new_groups = app.group.get_group_list()
    # Сравниваем длинну старого списка групп с новым
    assert len(old_groups) + 1 == len(new_groups)
