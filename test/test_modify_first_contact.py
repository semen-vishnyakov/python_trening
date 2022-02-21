from model.contact import Contact

def test_modify_first_contact_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(name="Semen1"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(name="testtest")
    contact.id = old_contacts[0].id
    app.contact.modify_first(contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

# def test_modify_first_contact_midname(app):
#     if app.contact.count() == 0:
#         app.contact.create(Contact(name="Semen1"))
#     old_contacts = app.contact.get_contact_list()
#     app.contact.modify_first(Contact(midname="testtest1"))
#     new_contacts = app.contact.get_contact_list()
#     assert len(old_contacts) == len(new_contacts)
