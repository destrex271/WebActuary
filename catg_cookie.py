from selenium_cookies import CatCookie
import json
from directory_create_module import create_dir


class CatgCookie:

    def __init__(self, url, folder):
        self.url = url
        self.folder_name = folder

    def cat_cook(self):
        ck = CatCookie(self.url, self.folder_name)
        cook = ck.get_cookies()
        domain_list = []
        cat_dict = {}

        for cookie in cook:
            dm = cookie["domain"]
            if not domain_list.__contains__(dm):
                domain_list.append(dm)

        for domain in domain_list:
            li = []
            for cookie in cook:
                if cookie["domain"] == domain:
                    li.append(cookie)

            cat_dict[domain] = li
        return cat_dict

    def conv_to_json(self):
        json_obj = json.dumps(self.cat_cook())
        self.write_to_file("cookie_acc_domain.json", json_obj)

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
