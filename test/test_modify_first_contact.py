from model.contact import Contact

def test_modify_first_contact_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(name="Semen1"))
    app.contact.modify_first(Contact(name="testtest"))

def test_modify_first_contact_midname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(name="Semen1"))
    app.contact.modify_first(Contact(midname="testtest1"))
