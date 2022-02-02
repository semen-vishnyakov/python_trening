# -*- coding: utf-8 -*-
from model.contact import Contact
    
def test_add_contact(app):
    app.contact.create(Contact(name="Semen1", midname="-", lastname="Vishnyakov",
                       nickname="Antigon", title="boss", company="Stenn",
                       address="Moscow", home_phone="3", mobile_phone="9852064950",
                       work_phone="QA", fax="-", email="semmmen8@gmail.com",
                       email2="-", email3="-", homepage="stenn.ru", bday="1", bmonth="January",
                       byear="1996", aday="1", amonth="January", ayear="2021", address2="-",
                       phone2="-", notes="-"))

def test_add_empty_contact(app):
    app.contact.create(Contact(name="", midname="", lastname="",
                       nickname="", title="", company="",
                       address="", home_phone="", mobile_phone="",
                       work_phone="", fax="", email="",
                       email2="", email3="", homepage="", bday="", bmonth="",
                       byear="", aday="", amonth="", ayear="", address2="",
                       phone2="", notes=""))