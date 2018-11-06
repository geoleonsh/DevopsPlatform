from flask_login import UserMixin
from databases import MySqliteDB


class User(UserMixin):
    def __init__(self, username):
        self.username = username
        self.DB = MySqliteDB()
        self.id = self.get_id()

    def is_matched(self, username, password):
        return self.DB.login_check(username, password)

    def get_id(self):
        if self.username is not None:
            user_id = self.DB.get_userid(self.username)
            return user_id
        else:
            return None

    @staticmethod
    def get(user_id):
        if not user_id:
            return None
        DB = MySqliteDB()
        user_name = DB.get_name_by_id(user_id)
        if user_name:
            return User(user_name)
        else:
            return None
