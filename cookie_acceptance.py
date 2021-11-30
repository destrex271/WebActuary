from markup_content import MarkupContent
from modal_cookie import Modal


final_dict = {}


class CookieConsent:

    def __init__(self, url):
        self.url = url

    def check_acc(self):
        mk = MarkupContent(self.url)
        ac = mk.get_markup_content()
        a_list = ac.find_all("a")
        b_list = ac.find_all("button")
        final_link_list = []
        final_button_list = []
        did_accept = False
        has_policy = False
        policy_link = ""

        for link in a_list:
            tx = link.text.lower()
            #print(link.text)
            if (tx.__contains__("cookies") or tx.__contains__("privacy")):
                has_policy = True
                try:
                    policy_link = link["href"]
                except KeyError:
                    policy_link = ""
                final_link_list.append(link)
            elif tx.__contains__("accept") and link.has_attr("href") and len(link["href"]) != 0 or (
                    tx.__contains__("manage") and tx.__contains__("cookies")) or (tx.__contains__("user") and tx.__contains__("agreement")):
                did_accept = True
                final_link_list.append(link)

        for button in b_list:
            tx = button.text.lower()
            #print(button.text)
            if tx.__contains__("cookies") or tx.__contains__("privacy"):
                has_policy = True
                final_button_list.append(button)
            elif tx.__contains__("accept") or tx.__contains__("continue") or tx.__contains__("cookies") or tx.__contains__(
                    "cookie") or (tx.__contains__("manage") and tx.__contains__("cookies")) or (tx.__contains__("ok") or tx.__contains__("yes") or tx.__contains__("got") or tx.__contains__("okay") or tx.__contains__("agree")):
                did_accept = True
                final_button_list.append(button)

        if len(final_link_list) == 0 and len(final_button_list) == 0:
            md = Modal(url=self.url)
            li = md.check_in_modal()
            if md.did_accept:
                did_accept = md.did_accept
            if md.has_policy:
                has_policy = md.has_policy
                policy_link = md.policy_link

        """if policy_link.__contains__("http"):
            did_accept = True
        else:
            has_policy = False"""

        final_dict = {
            "has_policy": has_policy,
            "did_accept": did_accept,
            "policy_link": policy_link,
        }
        print(final_dict)
        return final_dict
