import pandas as pd
from src.DataObjects.Category import Category
from src.DataAccessObjects.DataAccessObject import DataAccessObject


class CategoryDao(DataAccessObject):
    def __init__(self):
        super(CategoryDao, self).__init__(table_name='categories')

    def create_category(self, category:Category):
        category = {'name': category.name, 'description': category.description}
        return self.insert(values=category)

    def get_category_by_id(self, category_id:int):
        conditions = [{
            'column': 'id',
            'value': category_id,
            'operator': '=',
            'options': ''
        }]

        query_result = self.select(conditions=conditions)
        if query_result and query_result.first():
            return Category(id=query_result.value('id'), name=query_result.value('name'), description=query_result.value('description'))
        return None

    def get_category_by_name(self, category_name:str):
        conditions = [{
            'column': 'name',
            'value': category_name,
            'operator': '=',
            'options': ''
        }]

        query_result = self.select(conditions=conditions)
        if query_result and query_result.first():
            return Category(name=query_result.value('name'), description=query_result.value('description'))
        return None

    def get_all_categories(self):
        categories = []
        query_result = self.select()
        while(query_result.next()):
            categories.append(Category(name=query_result.value('name'), description=query_result.value('description')))
        return categories

    def update_category(self, category_id, values):
        conditions = [{
            'column': 'id',
            'value': category_id,
            'operator': '=',
            'options': ''
        }]
        return self.update(values=values, conditions=conditions)

    def delete_category(self, category_id:int):
        conditions = [{
            'column': 'id',
            'value': category_id,
            'operator': '=',
            'options': ''
        }]
        return self.delete(conditions=conditions)

    def get_categories_dataframe(self, conditions=''):
        categories = []
        categories_result = self.select(conditions=conditions)
        while categories_result.next():
            categories.append(Category(id=categories_result.value('id'),
                                       name=categories_result.value('name'),
                                       description=categories_result.value('description')).serialize_category())

        categories_dataframe = pd.DataFrame(categories)
        new_columns = [column.replace('_', ' ').capitalize() for column in categories_dataframe.columns]
        categories_dataframe.rename({categories_dataframe.columns[i]: new_columns[i] for i in range(len(new_columns))},
                                    axis=1, inplace=True)
        return categories_dataframe

    def get_data_for_completer(self, column):
        column_values = []
        column_results = self.select(columns=[column,])
        while column_results.next():
            column_values.append(str(column_results.value(column)))
        return column_values




