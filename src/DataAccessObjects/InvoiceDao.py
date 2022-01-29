from src.DataAccessObjects.DataAccessObject import DataAccessObject
from src.DataObjects.Invoice import Invoice


class InvoiceDao(DataAccessObject):
    def __init__(self, is_testing=False):
        super(InvoiceDao, self).__init__(table_name='invoices', is_testing=is_testing)

    def create_invoice(self, invoice):
        invoice_values = {'serial_number': invoice.get_serial_number(),
                          'date': invoice.get_date(),
                          'employee_id': invoice.get_employee().id,
                          'customer_id': invoice.get_customer().id}
        invoice_id = self.insert(values=invoice_values)
        return self.set_invoice_products(invoice_id, invoice.get_products()) if invoice_id > 0 else None

    def get_invoices(self, conditions, columns=['id', 'serial_number', 'date']):
        invoices = []
        invoices_result = self.select(columns=columns, conditions=conditions)
        while invoices_result.next():
            invoices.append(Invoice(invoice_id=invoices_result.value('id'),
                                    serial_number=invoices_result.value('serial_number'),
                                    date=invoices_result.value('date')))
        return invoices

    def set_invoice_products(self, invoice_id, products):
        return invoice_id if self.insert([{'invoice_id': invoice_id, 'product_id': product} for product in products],
                                         table_name='invoices_products') else -1

    def get_invoices_dataframe(self, conditions=None):
        query = f"""
        SELECT invoice.id AS invoice_id, invoice.serial_number AS serial_number, invoice.date AS invoice_date, 
        invoices_products.quantity AS quantity, SUM(products.price*invoices_products.quantity) AS total 
        FROM invoices AS invoice INNER JOIN invoices_products ON invoice.id=invoices_products.invoice_id 
        INNER JOIN products ON invoices_products.product_id=products.id GROUP BY(invoice_id) 
        {self.build_conditions(conditions) if conditions else ''}"""
        placeholders = self.extract_values_from_conditions(conditions) if conditions else None
        invoices_result = self.execute_select_query(query_str=query, placeholders=placeholders)
        invoices = []
        while invoices_result.next():
            invoices.append(Invoice(invoice_id=invoices_result.value('invoice_id'),
                                    serial_number=invoices_result.value('serial_number'),
                                    date=invoices_result.value('date')))
        return invoices




