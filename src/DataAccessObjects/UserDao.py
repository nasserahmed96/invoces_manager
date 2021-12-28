from src.DataAccessObjects.DataAccessObject import DataAccessObject
from src.DataObjects.User import User

class UserDao(DataAccessObject):
    def __init__(self):
        super(UserDao, self).__init__(table_name='users')

    def create_user(self, user:User):
        user_data = {
            'first_name': user.first_name,
            'middle_name': user.middle_name,
            'last_name': user.last_name,
            'phone_number': user.phone_number,
            'address': user.address,
            'gender': user.gender,
            'email': user.email,
            'notes': user.notes,
            'status': user.status
        }
        return self.insert(values=user_data)

    def get_all_users(self):
        users = []
        query_result = self.select()
        while(query_result.next()):
            users.append(self.fill_user(query_result))
        return users

    def get_user_by_id(self, user_id):
        conditions = [{
            'column': 'id',
            'value': user_id,
            'operator': '=',
            'options': '',
            'logic': ''
        },
        ]
        query_result = self.select(conditions=conditions)
        if query_result and query_result.first():
            return self.fill_user(query_result)
        return None

    def get_user_name(self, user_name):
        conditions = [
            {
                'column': 'first_name',
                'value': user_name,
                'operator': '=',
                'options': '',
                'logic': 'AND'
            },
            {
                'column': 'middle_name',
                'value': user_name,
                'operator': '=',
                'options': '',
                'logic': 'OR'
            },
            {
                'column': 'last_name',
                'value': user_name,
                'operator': '=',
                'options': '',
                'logic': 'OR'
            }
        ]
        query_result = self.select(conditions=conditions)
        if query_result and query_result.first():
            return self.fill_user(query_result)
        return None

    def fill_user(self, query_result):
        return User(first_name=query_result.value('first_name'),
                    middle_name=query_result.value('middle_name'),
                    last_name=query_result.value('last_name'),
                    phone_number=query_result.value('phone_number'),
                    address=query_result.value('address'),
                    gender=query_result.value('gender'),
                    email=query_result.value('email'),
                    notes=query_result.value('notes'),
                    status=query_result.value('status')
                    )
