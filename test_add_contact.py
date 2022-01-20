# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from application_contact import Application_contact

@pytest.fixture
def app(request):
    fixture = Application_contact()
    request.addfinalizer(fixture.destroy)
    return fixture
    
def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.creation_contact(Contact(name="Semen1", midname="-", lastname="Vishnyakov",
                                 nickname="Antigon", title="boss", company="Stenn",
                                 address="Moscow", home_phone="3", mobile_phone="9852064950",
                                 work_phone="QA", fax="-", email="semmmen8@gmail.com",
                                 email2="-", email3="-", homepage="stenn.ru", bday="1", bmonth="January",
                                 byear="1996", aday="1", amonth="January", ayear="2021", address2="-",
                                 phone2="-", notes="-"))
    app.logout()

def test_add_empty_contact(app):
    app.login(username="admin", password="secret")
    app.creation_contact(Contact(name="", midname="", lastname="",
                                 nickname="", title="", company="",
                                 address="", home_phone="", mobile_phone="",
                                 work_phone="", fax="", email="",
                                 email2="", email3="", homepage="", bday="", bmonth="",
                                 byear="", aday="", amonth="", ayear="", address2="",
                                 phone2="", notes=""))
    app.logout()