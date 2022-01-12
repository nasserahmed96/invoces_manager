
"""
NASSER
Prototyping script for doctor's medical prescription, which written to prototype the invoice and simulate the behaviour of the buying process
"""

import sys
import csv
import random
import datetime
from jinja2 import Environment, PackageLoader, select_autoescape
import pdfkit
import pandas as pd


"""
Get a date string and return date in the requested format, default is yyyy-mm-dd
"""

"""
Invoice input data:
-Invoice serial
-Customer name
-Employee name
-Product name
-Product brand
-Product price
-Required quantity
"""

"""
Invoice calculated data:
-Date time
-Total price
-Total products
-Total quantity
"""

def get_date(date, date_format=None):
    if not date_format:
        date_format = "%Y-%m-%d"
    return date.strftime(date_format)


def read_products(csv_file):
    products = pd.read_csv(csv_file, usecols=["name", "brand", "price", "quantity"])
    return products


def generate_invoice(products):
    RENDERED_TEMPLATES_PATH = "myapp/rendered_templates/"
    env = Environment(loader=PackageLoader("myapp"), autoescape=select_autoescape())
    template = env.get_template("invoice.html")
    invoice = dict()
    now = datetime.datetime.now()
    invoice["date"] = get_date(now.date())
    invoice["time"] = now.strftime("%H:%M")
    invoice["serial_no"] = random.randint(1000, 10000)

    parsed_products = []
    for key, product in products.iterrows():
        product['quantity'] = random.randint(1, 10)
        product['grand_total'] = product['price'] * product['quantity']
        parsed_products.append(product)
    rendered_page = template.render(products=parsed_products, invoice=invoice)

    with open(RENDERED_TEMPLATES_PATH + "invoice.html", "w") as output_file:
        output_file.write(rendered_page)

    pdfkit.from_file(RENDERED_TEMPLATES_PATH + "invoice.html", "test_invoice_new.pdf")


if __name__ == "__main__":
    program_name, *arguments = sys.argv
    file_name = ""
    if not arguments:
        print("Please provide a valid file name")
        file_name = input()
    else:
        file_name = arguments[0]
    products = read_products(file_name)[0:5]
    generate_invoice(products)
