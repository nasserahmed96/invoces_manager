from src.DataAccessObjects.DataAccessObject import DataAccessObject


class InvoiceDao(DataAccessObject):
    def __init__(self):
        super(InvoiceDao, self).__init__(table_name='invoices')

    def create_invoice(self, invoice):
        invoice_values = {'serial_number': invoice.get_serial_number(),
                          'date': invoice.get_date(),
                          'employee_id': invoice.get_employee().id,
                          'customer_id': invoice.get_customer().id}
        invoice_id = self.insert(values=invoice_values)
        return self.set_invoice_products(invoice_id, invoice.get_products()) if invoice_id > 0 else None

    def set_invoice_products(self, invoice_id, products):
        self.insert([{'invoice_id': invoice_id, 'product_id': product} for product in products],
                    table_name='invoices_products')

