class Customer(object):
    def __init__(self, id=None, user=None):
        self.id = id
        self.user = user

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_user(self):
        return self.user

    def set_user(self, user):
        self.user = user

    def __str__(self):
        return self.user