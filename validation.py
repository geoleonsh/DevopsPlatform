from databases import MySqliteDB


class Validation(object):
    def __init__(self):
        self.DB = MySqliteDB()

    def login_validation(self, username, password):
        return self.DB.login_check(username, password)
