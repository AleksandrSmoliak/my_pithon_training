# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app, db, json_groups):
    group = json_groups
    # Получаем текущий список групп (из БД)
    old_groups = db.get_group_list()
    # Добавляем новую группу
    app.group.create(group)
    # Получаем новый список групп (из БД)
    new_groups = db.get_group_list()
    # В переменную добавляем ту же самую группу, что добавили через интерфейс
    old_groups.append(group)
    # Проверка сравнения старой и новой группы
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)