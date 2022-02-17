from model.contact import Contact

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_creation_contact_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/edit.php") > 0):
            wd.find_element_by_link_text("add new").click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def change_field_data_value(self, field_name, text):
            wd = self.app.wd
            if text is not None:
                wd.find_element_by_name(field_name).click()
                wd.find_element_by_xpath(f"//option[@value='{text}']").click()

    def create(self, contact):
        wd = self.app.wd
        self.open_creation_contact_page()
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.return_to_home_page()

    def fill_contact_form(self, contact):
        self.change_field_value("firstname", contact.name)
        self.change_field_value("middlename", contact.midname)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home_phone)
        self.change_field_value("mobile", contact.mobile_phone)
        self.change_field_value("work", contact.work_phone)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        self.change_field_data_value("bday", contact.bday)
        self.change_field_data_value("bmonth", contact.bmonth)
        self.change_field_value("byear", contact.byear)
        self.change_field_data_value("aday", contact.aday)
        self.change_field_data_value("amonth", contact.amonth)
        self.change_field_value("ayear", contact.ayear)
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes)

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_contacts_page()
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()

    def open_contacts_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def modify_first(self, new_contact_data):
        wd = self.app.wd
        self.open_contacts_page()
        # init modify first contact
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_contact_form(new_contact_data)
        # submit contact modify
        wd.find_element_by_name("update").click()
        self.return_to_home_page()

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def count(self):
        wd = self.app.wd
        self.open_contacts_page()
        return len(wd.find_elements_by_name("selected[]"))

    def get_contact_list(self):
        wd = self.app.wd
        self.open_contacts_page()
        contacts_list = []
        for element in wd.find_elements_by_css_selector("tr.odd"):
            text = element.text
            id = element.find_element_by_name("selected[]").get_attribute("value")
            contacts_list.append(Contact(name = text, lastname = text, id = id))
        return contacts_list