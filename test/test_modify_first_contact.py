from model.contact import Contact

def test_modify_first_contact_name(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first(Contact(name="testtest"))
    app.session.logout()

def test_modify_first_contact_midname(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first(Contact(midname="testtest1"))
    app.session.logout()