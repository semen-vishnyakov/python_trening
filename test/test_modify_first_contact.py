from model.contact import Contact

def test_modify_first_contact_name(app):
    app.contact.modify_first(Contact(name="testtest"))

def test_modify_first_contact_midname(app):
    app.contact.modify_first(Contact(midname="testtest1"))
