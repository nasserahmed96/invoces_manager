import config
from src.DataAccessObjects.InvoiceDao import InvoiceDao
import datetime
import csv
from src.DataObjects.Invoice import Invoice
from src.DataObjects.Employee import Employee
from src.DataObjects.Customer import Customer


class InvoiceDaoTesting:
    def __init__(self):
        self.FILE_PATH = config.TEST_DATA_PATH + 'invoices_data_testing.csv'
        self.invoice_dao = InvoiceDao()

    def read_file(self):
        with open(self.FILE_PATH) as data_file:
            return list(csv.DictReader(data_file))

    def test_create_invoice(self):
        invoice = Invoice(serial_number=9893998564321,
                          date='2020-1-12',
                          employee=Employee(id=2),
                          customer=Customer(id=1),
                          products=[1, 65, 98, 36])

        print(self.invoice_dao.create_invoice(invoice))

    def run_tests(self):
        self.test_create_invoice()


if __name__ == '__main__':
    invoice_testing = InvoiceDaoTesting()
    invoice_testing.run_tests()


