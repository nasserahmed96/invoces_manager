class Category(object):
    def __init__(self, id=None, name=None, description=None):
        self.id = id
        self.name = name
        self.description = description

    def get_id(self):
        return self.id

    def set_id(self, id:int):
        self.id = id
        
    def get_name(self):
        return self.name

    def set_name(self, name:str):
        self.name = name

    def get_description(self):
        return self.name

    def set_description(self, description:str):
        self.description = description

    def __str__(self):
        return self.name