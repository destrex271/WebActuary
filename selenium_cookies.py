from selenium import webdriver
from collections import OrderedDict
from driver_solver import get_driver_path
from directory_create_module import create_dir
import json


class CatCookie:

    def __init__(self, url, folder):
        self.url = url
        self.folder_name = folder
        c_op = webdriver.ChromeOptions()
        c_op.add_argument("--headless")
        c_op.add_argument("--log-level=3")
        self.driver = webdriver.Chrome(executable_path=get_driver_path(), options=c_op)
        # self.driver = webdriver.PhantomJS("drivers/phantomjs/bin/phantomjs.exe")

    def get_cookies(self):
        self.driver.get(f'{self.url}')
        cookies = self.driver.get_cookies()
        return cookies

    def conv_to_json(self):
        ordered_dict = OrderedDict()
        ordered_dict = self.get_cookies()
        json_obj = json.dumps(ordered_dict)
        self.write_to_file("cookies.json", json_obj)
        return f"A Total of {len(ordered_dict)} were received"

    def write_to_file(self, file, content):
        """
        To write some given content to some given file
        :param file:
        :param content:
        :return:
        """
        with open(f"{self.folder_name}/{file}", "w") as f:
            f.write(content)
            f.close()
