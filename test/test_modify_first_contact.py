from model.contact import Contact

def test_modify_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first(Contact(name="abc", midname="-", lastname="abc",
                       nickname="abc", title="abc", company="abc",
                       address="abc", home_phone="12", mobile_phone="132123",
                       work_phone="-", fax="-", email="abc",
                       email2="-", email3="-", homepage="abc", bday="1", bmonth="January",
                       byear="1996", aday="1", amonth="January", ayear="2021", address2="-",
                       phone2="-", notes="-"))
    app.session.logout()