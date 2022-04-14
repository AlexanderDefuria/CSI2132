import flask_login
from db import DB

db = DB()


class User(flask_login.UserMixin):
    id = ""
    role = ""
    username = ""

    def __init__(self, username):
        if len(db.query('SELECT "id" FROM "User" WHERE username=\'' + str(username) + '\';')) > 0:
            self.id = db.query('SELECT "id" FROM "User" WHERE username=\'' + str(username) + '\';')[0][0]
            self.username = username
            if len(db.query('SELECT "role" FROM "Employee" WHERE user_id=' + str(self.id) + ';')) > 0:
                self.role = db.query('SELECT "role" FROM "Employee" WHERE user_id=' + str(self.id) + ';')
            elif len(db.query('SELECT "user_id" FROM "ResponsibleUser" WHERE user_id=' + str(self.id) + ';')) > 0:
                self.role = "ResponsibleUser"
            else:
                self.role = "Patient"

    def is_authenticated(self):
        return False

    def is_active(self):
        pass

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id
