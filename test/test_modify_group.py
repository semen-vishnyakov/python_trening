from model.group import Group

def test_modify_first_group_name(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first(Group(name="name1"))
    app.session.logout()

def test_modify_first_group_header(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first(Group(header="header1"))
    app.session.logout()