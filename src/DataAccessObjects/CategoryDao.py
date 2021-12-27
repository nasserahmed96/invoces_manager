from src.DataObjects.Category import Category
from src.DataAccessObjects.DataAccessObject import DataAccessObject


class CategoryDao(DataAccessObject):
    def __init__(self):
        super(CategoryDao, self).__init__(table_name='categories')

    def create_category(self, category:Category):
        category = {'name': category.name, 'description': category.description}
        self.insert(values=category)

    def get_category_by_id(self, category_id:int):
        conditions = [{
            'column': 'id',
            'operator': '=',
            'options': ''
        }]
        values = {
            'id': category_id
        }
        query_result = self.select(conditions=conditions, placeholders=values)
        if query_result and query_result.first():
            return Category(name=query_result.value('name'), description=query_result.value('description'))
        return None

    def get_category_by_name(self, category_name:str):
        conditions = [{
            'column': 'name',
            'operator': '=',
            'options': ''
        }]
        values = {
            'name': category_name
        }
        query_result = self.select(conditions=conditions, placeholders=values)
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
            'operator': '=',
            'options': ''
        }]
        values['id'] = category_id
        return self.update(values=values, conditions=conditions)

    def delete_category(self, category_id:int):
        conditions = [{
            'column': 'id',
            'operator': '=',
            'options': ''
        }]
        placeholders = {
            'id': category_id
        }
        return self.delete(conditions=conditions, placeholders=placeholders)



