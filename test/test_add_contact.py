# -*- coding: utf-8 -*-
from model.contact import Contact
    
def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(name="Semen1", midname="-", lastname="Vishnyakov",
                       nickname="Antigon", title="boss", company="Stenn",
                       address="Moscow", home_phone="3", mobile_phone="9852064950",
                       work_phone="QA", fax="-", email="semmmen8@gmail.com",
                       email2="-", email3="-", homepage="stenn.ru", bday="1", bmonth="January",
                       byear="1996", aday="1", amonth="January", ayear="2021", address2="-",
                       phone2="-", notes="-")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

# def test_add_empty_contact(app):
#     old_contacts = app.contact.get_contact_list()
#     contact = Contact(name="", midname="", lastname="",
#                        nickname="", title="", company="",
#                        address="", home_phone="", mobile_phone="",
#                        work_phone="", fax="", email="",
#                        email2="", email3="", homepage="", bday="", bmonth="",
#                        byear="", aday="", amonth="", ayear="", address2="",
#                        phone2="", notes="")
#     app.contact.create(contact)
#     new_contacts = app.contact.get_contact_list()
#     assert len(old_contacts) + 1 == len(new_contacts)
#     old_contacts.append(contact)
#     assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)