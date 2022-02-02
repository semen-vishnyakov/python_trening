from model.group import Group

def test_modify_first_group_name(app):
    app.group.modify_first(Group(name="name1"))

def test_modify_first_group_header(app):
    app.group.modify_first(Group(header="header1"))
