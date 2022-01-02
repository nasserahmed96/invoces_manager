
class Employee:
    def __init__(self, id=None, user=None, username=None):
        self.id = id
        self.user = user
        self.username = username

    def get_id(self):
        return self._id

    def set_id(self, id):
        self.id = id

    def get_user(self):
        return self.user

    def set_user(self, user):
        self.user = user

    def get_username(self):
        return self.username

    def set_username(self, username):
        self.username = username

    def serialize_employee(self):
        user_dict = self.__dict__.pop('user').__dict__
        self.__dict__.update(user_dict)
        return self.__dict__

