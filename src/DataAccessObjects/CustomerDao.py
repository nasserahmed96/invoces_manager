from src.DataAccessObjects.DataAccessObject import DataAccessObject
from src.DataAccessObjects.UserDao import UserDao
from src.DataObjects.Customer import Customer

class CustomerDao(DataAccessObject):
    def __init__(self):
        super(CustomerDao, self).__init__(table_name='customers')
        self.user_dao = UserDao()

    def create_customer(self, customer:Customer):
        values = {
            'user_id': self.user_dao.create_user(customer.user)
        }
        return self.insert(values=values)

    def update_customer(self, customer_id, values):
        user_id = self.get_customer_user(customer_id)
        user_values = values.pop('user')
        print('user_values: ', user_values)
        return self.user_dao.update_user(user_id, values=user_values)

    def get_all_customers(self):
        customers = []
        query = """SELECT users.*, customers.id AS customer_id FROM customers INNER JOIN users ON users.id=customers.user_id"""
        query_result = self.execute_select_query(query_str=query)
        while(query_result.next()):
            customers.append(Customer(user=self.user_dao.fill_user(query_result), id=query_result.value('customer_id')))
        return customers


    def get_customer_user(self, customer_id):
        user_id = self.select(columns=['user_id'], conditions=[{
            'column': 'id',
            'value': customer_id,
            'operator': '=',
            'options': '',
            'logic': ''
        }])
        if user_id and user_id.first():
            return user_id.value('user_id')
        return None

    def get_customer_by_id(self, customer_id):
        conditions = [{
            'column': 'id',
            'value': customer_id,
            'operator': '=',
            'options': ''
        }]
        customer = self.select(conditions=conditions)
        if customer and customer.first():
            return Customer(user=self.user_dao.get_user_by_id(customer.value('user_id')))
        return None

    def delete_customer(self, customer_id):
        user_id = self.get_customer_user(customer_id)
        self.user_dao.delete_user(user_id=user_id)
        return self.delete(conditions=[{
            'column': 'id',
            'value': customer_id,
            'operator': '=',
            'options': ''
        }])