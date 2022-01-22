from abc import ABCMeta, abstractmethod
import pdfkit
from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader
from jinja2.exceptions import TemplateNotFound
import pandas as pd
import config


class Report(metaclass=ABCMeta):
    def __init__(self, stylesheet, template_name, output_path):
        self.root_path = config.REPORTS_ROOT_PATH
        self.templates_root_path = self.root_path + 'Templates/'
        self.raw_templates_path = self.templates_root_path + 'Raw_Templates/'
        self.rendered_templates_path = self.templates_root_path + 'Rendered_Templates/'
        self.static_files_path = self.root_path + 'Static/'
        self.css_files_path = self.static_files_path + 'CSS/'
        self.template_name = template_name
        self.stylesheet = stylesheet
        self.output_path = output_path

    def set_template_name(self, template_name):
        self.template_name = template_name

    def get_template_name(self):
        return self.template_name

    def set_stylesheet(self, stylesheet):
        self.stylesheet = self.css_files_path + stylesheet

    def get_stylesheet(self):
        return self.stylesheet

    def set_output_path(self, output_path):
        self.output_path = output_path

    def get_output_path(self):
        return self.output_path

    def read_items(self, csv_file, cols):
        items = pd.read_csv(csv_file, usecols=cols)
        self.items = items

    def get_template(self):
        env = Environment(loader=FileSystemLoader(self.raw_templates_path), autoescape=select_autoescape())
        return env.get_template(self.template_name)
    
    """
    This function must be overriden in order to function
    """
    @abstractmethod
    def render_report(self):
        pass

    def generate_report(self):
        options = {"page-size": "A4",
                   "margin-left": "0",
                   "margin-right": "0",
                   "margin-top": "0",
                   "margin-bottom": "0",
                   "orientation": "Portrait",
                   "encoding": "UTF-8",
                   "quiet": "",
                   }
        pdfkit.from_file(self.rendered_templates_path + self.template_name, self.output_path,
                         css=self.css_files_path + self.stylesheet, options=options)

    def save_rendered_page(self, rendered_page):
        print('Save invoice to: ', self.rendered_templates_path+self.template_name)
        with open(self.rendered_templates_path + self.template_name, "w") as output_file:
            output_file.write(rendered_page)