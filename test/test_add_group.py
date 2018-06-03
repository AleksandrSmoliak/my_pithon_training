# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.group.create(Group(name="Group1", header="Group1_Header", footer="Group1_Footer"))


def test_add_group_empty(app):
    app.group.create(Group(name="", header="", footer=""))

