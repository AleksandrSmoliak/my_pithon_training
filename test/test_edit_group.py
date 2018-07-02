from model.group import Group
from random import randrange



def test_edit_first_group_name(app, db):
    # Если список групп отсутствует его необходимо создать
    if app.group.count() == 0:
        app.group.create(Group(name="Group1", header="Group1_Header", footer="Group1_Footer"))
    # Получение списка групп из пользовательского интерфейса
    #old_groups = app.group.get_group_list()
    # Получение списка групп из БД
    old_groups = db.get_group_list()
    # Генерируем индекс в пределах полученного списка
    index = randrange(len(old_groups))
    # Создаем новый объект по которому будут изменения
    group = Group(name="Edit_name", header="Group1_Header", footer="Group1_Footer")
    # Получаем ид элемента у у объекта с сгенерированным индексом
    group.id = old_groups[index].id
    # Изменяем выбранный элемент
    app.group.edit_group_by_index(group, index)
    # Получение списка групп из пользовательского интерфейса
    #new_groups = app.group.get_group_list()
    new_groups = db.get_group_list()
    # Сравнивваем длинну списков до изменения и после изменения
    assert len(old_groups) == len(new_groups)
    # Присваиваем рпанее полученному объекту с выбранным индексом новое значение поля
    old_groups[index] = group
    # Сравниваем отсортированные списки групп до изменения и после
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_edit_first_group_header(app, db):
    if app.group.count() == 0:
        app.group.create(Group(name="Group1", header="Group1_Header", footer="Group1_Footer"))
    #old_groups = app.group.get_group_list()
    old_groups = db.get_group_list()
    app.group.edit_first_group(Group(header="Edit_Header"))
    #new_groups = app.group.get_group_list()
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_edit_first_group_footer(app, db):
    if app.group.count() == 0:
        app.group.create(Group(name="Group1", header="Group1_Header", footer="Group1_Footer"))
    #old_groups = app.group.get_group_list()
    old_groups = db.get_group_list()
    app.group.edit_first_group(Group(footer="Edit_Footer"))
    #new_groups = app.group.get_group_list()
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)