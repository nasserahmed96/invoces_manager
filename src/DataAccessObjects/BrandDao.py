from PyQt5.QtSql import QSqlQuery
from src.DataObjects.Brand import Brand
from src.DataAccessObjects.DataAccessObject import DataAccessObject
import pandas as pd


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

    def get_brands_dataframe(self, conditions=''):
        brands = []
        brands_result = self.select()
        while brands_result.next():
            brands.append(Brand(id=brands_result.value('id'),
                                name=brands_result.value('name'),
                                description=brands_result.value('description')).serialize_brand())
        brands_dataframe = pd.DataFrame(brands)
        new_columns = [column.replace('_', ' ').capitalize() for column in brands_dataframe.columns]
        brands_dataframe.rename({brands_dataframe.columns[i]: new_columns[i] for i in range(len(new_columns))},
                                   axis=1, inplace=True)
        return brands_dataframe








