from utilities.db.db_manager import dbManager


class ContactUs_users:

    def __init__(self, email, contact,user_name):
        super().__init__()
        self.email = email
        self.contact = contact
        self.user_name = user_name

    def add_contact(self):
        query = "INSERT INTO contactus(email, contact, user_name) VALUES ('%s', '%s', '%s')" % (
            self.email, self.contact, self.user_name)
        query_result = dbManager.commit(query)
        print(query_result)
