from datetime import datetime

from utilities.db.db_manager import dbManager


class User:
    def __init__(self, email, account_name, password, phone_number, first_name, last_name, Age, first_time, destination,
                 start_date, end_date, language, budget, hobbies, vibe, filename, about_me, facebook, instagram):
        super().__init__()
        self.email = email
        self.account_name = account_name
        self.password = password
        self.phone = phone_number
        self.first_name = first_name
        self.last_name = last_name
        self.Age = Age
        self.first_time = bool(first_time)
        self.destination = destination
        self.start_date = start_date
        self.end_date = end_date
        self.language = language
        self.budget = budget
        self.hobbies = hobbies
        self.vibe = vibe
        self.filename = filename
        self.about = about_me
        self.facebook = facebook
        self.instagram = instagram

    def add_user(self):
        query = "INSERT INTO users(email, Account_name, password, phone) VALUES ('%s', '%s', '%s', %s)" % (
            self.email, self.account_name, self.password, self.phone)
        query_result = dbManager.commit(query)
        print(query_result)

    def search_user(self):
        query = f"select * from users where email='%s'" % self.email
        query_result = dbManager.fetch(query)
        return query_result

    def update_user(self):
        query = f"UPDATE users set first_name='%s', last_name='%s', Age='%s',first_time='%s',destination='%s',start_date='%s',end_date='%s',language='%s',budget=%s,hobbies='%s',vibe='%s',URL_pic='%s',facebook='%s',instagram='%s',about_me='%s' where email='%s'" % \
                (self.first_name, self.last_name, self.Age, self.first_time, self.destination, self.start_date,
                 self.end_date, self.language, self.budget, self.hobbies,
                 self.vibe, self.filename, self.facebook, self.instagram, self.about, self.email)
        query_result = dbManager.commit(query)

