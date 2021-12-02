import sys
import time

import requests.exceptions
from requests import get
from bs4 import BeautifulSoup
import ssl
from directory_create_module import create_dir


class MarkupContent:

    def __init__(self, url):
        self.url = url
        self.ls = 0
        self.lt = 0

    def get_markup_content(self):
        try:
            response = get(self.url)

        except ConnectionError:
            if self.ls <= 3:
                self.get_markup_content()
                self.ls += 1
        except ssl.SSLError:
            if self.lt <= 3:
                self.get_markup_content()
                self.lt += 1

        html_soup = BeautifulSoup(response.text, 'html.parser')
        return html_soup

    def label_content(self):
        y = self.get_markup_content().prettify()
        list_num = [item for item in range(0, len(y.splitlines()))]
        return list_num
