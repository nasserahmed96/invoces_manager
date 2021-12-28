class User(object):
    def __init__(self, id=None, first_name=None, middle_name=None, last_name=None, phone_number=None,
                 address=None, gender=None, email=None, notes= None, status=None):
        self.id = id
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.address = address
        self.gender = gender
        self.email = email
        self.notes = notes
        self.status = status

    def get_id(self):
        return self.id

    def set_id(self, id:int):
        self.id = id

    def get_first_name(self):
        return self.first_name

    def set_first_name(self, first_name):
        self.first_name = first_name

    def get_middle_name(self):
        return self.middle_name

    def set_middle_name(self, middle_name):
        self.middle_name = middle_name

    def get_last_name(self):
        return self.last_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def get_phone_number(self):
        return self.phone_number

    def set_phone_number(self, phone_number):
        self.phone_number = phone_number

    def get_address(self):
        return self.address

    def set_address(self, address):
        self.address = address

    def get_gender(self):
        return self.gender

    def set_gender(self, gender):
        self.gender = gender

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    def get_notes(self):
        return self.notes

    def set_notes(self, notes):
        self.notes = notes

    def get_status(self):
        return self.status

    def set_status(self, status):
        self.status = status

    def __str__(self):
        return self.first_name + " " + self.last_name







