from model.group import Group

def test_modify_first_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.modify_first(Group(name="name1"))

def test_modify_first_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.modify_first(Group(header="header1"))
