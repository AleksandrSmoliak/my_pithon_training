# -*- coding: utf-8 -*-
from group import Group
import pytest
from Application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="Group1", header="Group1_Header", footer="Group1_Footer"))
    app.logout()


def test_add_group_empty(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()
