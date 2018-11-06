import sqlite3


class MySqliteDB(object):
    def connect_db(self):
        return sqlite3.connect('devops.db')

    def get_userid(self, UserName):
        conn = self.connect_db()
        cursor = conn.cursor()
        cursor.execute('SELECT UID FROM admin_users WHERE USERNAME=?', (UserName,))
        uid = cursor.fetchall()
        if uid:
            conn.close()
            return uid[0][0]
        else:
            return None

    def get_name_by_id(self, user_id):
        conn = self.connect_db()
        cursor = conn.execute('SELECT USERNAME FROM admin_users WHERE UID=?', (user_id,))
        user_name = cursor.fetchall()
        if user_name:
            conn.close()
            return user_name[0][0]
        else:
            return None

    def login_check(self, UserName, PassWord):
        conn = self.connect_db()
        cursor = conn.execute('SELECT USERNAME,PASSWORD FROM admin_users WHERE USERNAME=? AND PASSWORD=?', (UserName,
                                                                                                            PassWord))
        user_table = [dict(user=row[0], password=row[1]) for row in cursor]
        conn.close()
        if user_table:
            return True
        else:
            return False

    def add_admin_user(self, UserName, PassWord, Email, Phone):
        conn = self.connect_db()
        cursor = conn.cursor()
        cursor.execute('SELECT USERNAME FROM admin_users WHERE USERNAME=?', (UserName,))
        user_table = [dict(user=row[0]) for row in cursor]
        if user_table:
            return False
        else:
            cursor.execute('INSERT INTO admin_users(USERNAME,PASSWORD,EMAIL,PHONE) VALUES(?,?,?,?)',
                           (UserName, PassWord, Email, Phone))
            conn.commit()
            conn.close()
            return True

    def del_admin_user(self, UserName):
        conn = self.connect_db()
        cursor = conn.cursor()
        cursor.execute('SELECT USERNAME FROM admin_users WHERE USERNAME=?', (UserName,))
        user_table = [dict(user=row[0]) for row in cursor]
        if user_table:
            cursor.execute('DELETE FROM admin_users WHERE USERNAME=?', (UserName,))
            conn.commit()
            conn.close()
            return True
        else:
            return False

    def update_admin_user(self, UserName, PassWord, Email, Phone, UpdateTime):
        conn = self.connect_db()
        cursor = conn.cursor()
        cursor.execute('UPDATE admin_users SET USERNAME=?,PASSWORD=?,EMAIL=?,PHONE=?,UPDATETIME=? WHERE USERNAME=?',
                       (UserName, PassWord, Email, Phone, UpdateTime, UserName))
        conn.commit()
        conn.close()

    def list_admin_user(self):
        conn = self.connect_db()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM admin_users')
        user_table = [dict(uid=row[0], username=row[1], password=row[2], email=row[3], phone=row[4], addtime=row[5],
                           updatetime=row[6]) for row in cursor]
        conn.close()
        return user_table
