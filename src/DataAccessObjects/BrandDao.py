from PyQt5.QtSql import QSqlQuery
from src.DataObjects.Brand import Brand
from src.DataAccessObjects.DataAccessObject import DataAccessObject


class BrandDao(DataAccessObject):
    def __init__(self):
        super(BrandDao, self).__init__(table_name='brands')

    def create_brand(self, brand:Brand):
        values = {'name': brand.name, 'description': brand.description}
        return self.insert(values)

    def get_brand_by_id(self, id:int):
        conditions = [{
            'column': 'id',
            'value': id,
            'operator': '=',
            'options': ''
        }]
        query = self.select(conditions=conditions)
        if query and query.first():
            return Brand(id=query.value("id"), name=query.value("name"), description=query.value("description"))
        return None

    def get_brand_by_name(self, brand_name):
        conditions = [{
            'column': 'name',
            'value': brand_name,
            'operator': '=',
            'options': ''
        }]
        query = self.select(conditions=conditions)
        if query and query.first():
            return Brand(id=query.value("id"), name=query.value("name"), description=query.value("description"))
        return None

    def update_brand(self, brand_id, values):
        conditions = [{
            'column': 'id',
            'value': brand_id,
            'operator': '=',
            'options': ''
        }]
        return self.update(values=values, conditions=conditions)

    def delete_brand(self, brand_id:int):
        conditions = [{
            'column': 'id',
            'value': brand_id,
            'operator': '=',
            'options': ''
        }]
        return self.delete(conditions=conditions)

    def get_all_brands(self):
        query_result = self.select()
        self.brands = []
        while(query_result.next()):
            self.brands.append(Brand(id=query_result.value("id"),
                                     name=query_result.value("name"),
                                     description=query_result.value("description")))
        return self.brands




