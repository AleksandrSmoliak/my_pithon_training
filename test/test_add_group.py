# -*- coding: utf-8 -*-
from model.group import Group
import pytest


def test_add_group(app, db, json_groups):
    group = json_groups
    with pytest.allure.step('Получаем текущий список групп (из БД)'):
        old_groups = db.get_group_list()
    with pytest.allure.step('Добавляем новую группу %s ' % group):
        app.group.create(group)
    with pytest.allure.step('Получаем новый список групп (из БД)'):
        new_groups = db.get_group_list()
    with pytest.allure.step('В переменную добавляем ту же самую группу, что добавили через интерфейс'):
        old_groups.append(group)
    with pytest.allure.step('Проверка сравнения старой и новой группы'):
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)