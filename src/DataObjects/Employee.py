
class Employee:
    def __init__(self, id=None, user=None, username=None):
        self._id = id
        self._user = user
        self._username = username

    def get_id(self):
        return self._id

    def set_id(self, id):
        self._id = id

    def get_user(self):
        return self._user

    def set_user(self, user):
        self._user = user

    def get_username(self):
        return self._username

    def set_username(self, username):
        self._username = username

