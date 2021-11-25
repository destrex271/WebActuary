from directory_create_module import create_dir
import json
from selenium_cookies import CatCookie
from cookie_acceptance import CookieConsent
from validate_url import is_valid
from catg_cookie import CatgCookie


class CookieModule:

    def __init__(self, url):
        self.url = url
        self.final_dict = {}
        self.folder_name = "cookies"
        create_dir(self.folder_name)

    def gen_all_json(self):
        cat_cook = CatCookie(self.url, folder=self.folder_name)
        m = cat_cook.get_cookies()
        if len(m) != 0:
            cat_cook.conv_to_json()
            cc = CookieConsent(self.url)
            dc = cc.check_acc()
            """
            ::keyword::
                has_policy
                did_accept
                policy_link
            """
            vd = False
            if dc['policy_link'].__contains__('privacy'):
                dc['has_policy'] = False
            if len(dc["policy_link"].strip()) == 0:
                vd = False
            elif is_valid(dc["policy_link"]) == True:
                vd = True
            self.final_dict = {
                "has_policy": dc["has_policy"],
                "did_accept": dc["did_accept"],
                "policy_link": dc["policy_link"],
                "is_policy_valid": vd,
                'total_cookies': len(m)
            }
        else:
            self.final_dict = {
                "has_policy": False,
                "did_accept": False,
                "policy_link": '',
                "is_policy_valid": False,
                'total_cookies': 0
            }


    def conv_to_json(self):
        json_obj = json.dumps(self.final_dict)
        self.write_to_file("cookie_consent.json", json_obj)

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

    def cat_acc_domain(self):
        cg = CatgCookie(url=self.url, folder=self.folder_name)
        cg.cat_cook()
        cg.conv_to_json()
