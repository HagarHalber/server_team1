from utilities.db.db_manager import dbManager


class ContactUs_guest:

    def __init__(self, name, phone, email, contact):
        super().__init__()
        self.email = email
        self.contact = contact
        self.name = name
        self.phone = phone

    def add_contact(self):
        query = "INSERT INTO contactus_guest(name, email, phone, contact) VALUES ('%s', '%s', '%s','%s')" % (
            self.name, self.email, self.phone,self.contact)
        query_result = dbManager.commit(query)
        print(query_result)
