# -*- coding: utf-8 -*-
from model.contact import Contact
from fixtura.application import Application
import pytest

@pytest.fixture
def app(request):
    fixture=Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_new_contact(app):
    app.login(username="admin", password="secret")
    app.add_new_contact(Contact(firstname="Alina", middlename="Maratovna",lastname="Sapaeva", nickname="hhh",title="gsdhfg",
company="ggygg", address="gyfhg", home="frrg", mobile="9030620645",  work="gfgdghyfyu", fax="ggfgf", email="gyfgf",   email2="gdtr",
email3="nbjhg", homepage="ggfdghb",bday="12", bmonth="March", byear="1994", aday="17", amonth="May", ayear="2000", address2="gffgjf",
phone2 ="fygfsdf",  notes="hgk"))
    app.logout()

def test_add_empty_contact(app):
    app.login(username="admin", password="secret")
    app.add_new_contact(Contact(firstname="", middlename="",lastname="", nickname="",title="",
company="", address="", home="", mobile="",  work="", fax="", email="",   email2="",
email3="", homepage="",bday="-", bmonth="-", byear="-", aday="-", amonth="-", ayear="-", address2="",
phone2 ="",  notes=""))
    app.logout()







