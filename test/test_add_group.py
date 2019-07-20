# -*- coding: utf-8 -*-
from model.group import Group
from fixtura.application import Application
from fixtura.session import SessionHelper
import pytest

@pytest.fixture
def app(request):
    fixture=Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create( Group(name="test", header="test11", footer="test22"))
    app.session.logout()

def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create( Group(name="", header="", footer=""))
    app.session.logout()

