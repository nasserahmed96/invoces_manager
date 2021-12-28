from src.DataAccessObjects.DataAccessObject import DataAccessObject
from src.DataAccessObjects.CategoryDao import CategoryDao
from src.DataAccessObjects.BrandDao import BrandDao
from src.DataObjects.Product import Product

class ProductDao(DataAccessObject):
    def __init__(self):
        super(ProductDao, self).__init__(table_name='products')
        self.category_dao = CategoryDao()
        self.brand_dao = BrandDao()


    def create_product(self, product):
        print('Category ID: ', product.category.get_id())
        product_values = {
            'id': product.id,
            'name': product.name,
            'description' : product.description,
            'price' : product.price,
            'quantity' : product.quantity,
            'barcode' : product.barcode,
            'notes' : product.notes,
            'category' : product.category.get_id() if product.category else '',
            'brand' : product.brand.get_id() if product.brand else '',
            'status' : product.status if product.status else ''
        }
        self.insert(values=product_values)

    def get_all_products(self):
        products = []
        query_result = self.select()
        while(query_result.next()):
            products.append(self.fill_product(query_result))
        return products

    def get_product_by_id(self, product_id:int):
        conditions = [{
            'column': 'id',
            'value': product_id,
            'operator': '=',
            'options': ''
        }]

        product = self.select(conditions=conditions)
        if product and product.first():
            return self.fill_product(product)
        return None

    def fill_product(self, query_result):
        return Product(id=query_result.value('id'),
                        name=query_result.value('name'),
                        description=query_result.value('description'),
                        price=query_result.value('price'),
                        quantity=query_result.value('quantity'),
                        barcode=query_result.value('barcode'),
                        notes=query_result.value('notes'),
                        category=self.category_dao.get_category_by_id(query_result.value('id')),
                        brand=self.brand_dao.get_brand_by_id(query_result.value('id')),
                        status=query_result.value('status')
                        )

    def get_product_by_name(self, product_name:str):
        conditions = [{
            'column': 'name',
            'operator': '=',
            'options': ''
        }]
        placeholders = {
            'name': product_name
        }
        product = self.select(conditions=conditions, placeholders=placeholders)
        if product and product.first():
            return self.fill_product(product)
        return None

    def update_product(self, product_id, values):
        conditions = [{
            'column': 'id',
            'value': product_id,
            'operator': '=',
            'options': ''
        }]
        return self.update(values=values, conditions=conditions)

    def delete_product(self, product_id):
        conditions = [{
            'column': 'id',
            'value': product_id,
            'operator': '=',
            'options': ''
        }]
        return self.delete(conditions=conditions)



