import flask_login


class User(flask_login.UserMixin):
    id = ""
    role = ""

    def __init__(self, id):
        self.id = id

    def get(id):
        return User(id)

    def is_authenticated(self):
        return False

    def is_active(self):
        pass

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id