import sys
import csv
import random
import datetime
from jinja2 import Environment, PackageLoader, select_autoescape
import pdfkit
import pandas as pd
import base64

import config
from src.Reports.report import Report


"""
Invoice input data:
-Formatted date
-Invoice serial
-Customer name
-List of products includes(Product name, Product description, Quantity, Total for each product)
-Accessories
-After installation expencies
"""


class InvoiceReport(Report):
    def __init__(self, invoice_path, invoice_serial, customer_name, date, products_dataframe, accessories, above_installation, invoice_total):
        super(InvoiceReport, self).__init__(template_name='invoice.html', output_path=invoice_path, stylesheet='style.css')
        self.invoice_path = invoice_path
        self.invoice_serial = invoice_serial
        self.customer_name = customer_name
        self.date = date
        self.products_data = products_dataframe
        self.accessories = accessories
        self.above_installation = above_installation
        self.invoice_total = invoice_total

    def convert_dataframe_to_list(self, dataframe):
        """
        Convert the provided dataframe into a list of dictionaries
        :return:
        """
        dics = []
        for i in range(dataframe.shape[0]):
            dic = dict()
            for col in range(len(dataframe.columns)):
                dic[dataframe.columns[col]] = dataframe.iat[i, col]
            dics.append(dic)
        return dics

    def render_report(self):
        self.save_rendered_page(self.get_template().render(customer_name=self.customer_name,
                                                           products=self.products_data,
                                                           invoice_serial=self.invoice_serial,
                                                           date=self.date,
                                                           accessories=self.accessories,
                                                           above_installation=self.above_installation,
                                                           invoice_total=self.invoice_total,
                                                           company_icon=self.get_base64_image(config.ICON_PATH)))


    def get_base64_image(self, image_path):
        """
        :param image_path: Absolute image path
        :return: A string represents base64 image of the image
        """
        with open(image_path, 'rb') as image_file:
            image_string = base64.b64encode(image_file.read())
        return f'data:image/png;base64,{image_string.decode("UTF-8")}'





"""def generate_invoice(products):
    RENDERED_TEMPLATES_PATH = "myapp/rendered_templates/"
    env = Environment(loader=PackageLoader("myapp"), autoescape=select_autoescape())
    template = env.get_template("invoice.html")
    invoice = dict()
    now = datetime.datetime.now()

    parsed_products = []
    for key, product in products.iterrows():
        product['quantity'] = random.randint(1, 10)
        product['grand_total'] = product['price'] * product['quantity']
        parsed_products.append(product)
    rendered_page = template.render(products=parsed_products, invoice=invoice)

    with open(RENDERED_TEMPLATES_PATH + "invoice.html", "w") as output_file:
        output_file.write(rendered_page)

    pdfkit.from_file(RENDERED_TEMPLATES_PATH + "invoice.html", "test_invoice_new.pdf")"""


if __name__ == "__main__":
    products = [{
        'Name': 'Test invoice',
        'Description': 'Test new report class',
        'Price': 21.5,
        'Quantity': 2,
        'Total': 43
    }]
    products_dataframe = pd.DataFrame(products)
    print(products_dataframe)
    invoice = InvoiceReport(invoice_path='/home/nasser/refactor_invoice.pdf',
                            invoice_serial='5648978972132',
                            customer_name='Nasser',
                            date='20/1/2022',
                            products_dataframe=products_dataframe,
                            accessories=54,
                            above_installation=10,
                            invoice_total=107)
    invoice.render_report()
    invoice.generate_report()