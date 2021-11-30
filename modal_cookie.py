import sys
import bs4 as bs
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEnginePage
from PyQt5.QtWidgets import QApplication



class Page(QWebEnginePage):
    def __init__(self, url):
        self.app = QApplication(sys.argv)
        QWebEnginePage.__init__(self)
        self.html = ''
        self.loadFinished.connect(self._on_load_finished)
        self.load(QUrl(url))
        self.app.exec_()

    def _on_load_finished(self):
        self.html = self.toHtml(self.Callable)

    def Callable(self, html_str):
        self.html = html_str
        self.app.quit()


class Modal:

    def __init__(self, url):
        self.url = url
        self.did_accept = False
        self.has_policy = False
        self.policy_link = ""

    def check_in_modal(self):
        page = Page(f'{self.url}')
        soup = bs.BeautifulSoup(page.html, 'html.parser')
        link_list = soup.find_all("a")
        button_list = soup.find_all("button")
        final_list = []
        for link in link_list:
            tx = link.text.lower()
            if (tx.__contains__("cookies") or tx.__contains__("cookie") or tx.__contains__("privacy")) and tx.__contains__("policy"):
                self.has_policy = True
                self.policy_link = link["href"]
                final_list.append(link)
            elif tx.__contains__("accept") and link.has_attr("href") and len(link["href"]) != 0 or (tx.__contains__("manage") and tx.__contains__("cookies")):
                self.did_accept = True
                final_list.append(link)

        for button in button_list:
            tx = button.text.lower()
            if (tx.__contains__("cookies") or tx.__contains__("privacy")) and tx.__contains__("policy"):
                self.has_policy = True
                final_list.append(button)
            elif tx.__contains__("accept") or tx.__contains__("cookies") or tx.__contains__(
                    "cookie") or (tx.__contains__("manage") and tx.__contains__("cookies")) or (tx.__contains__("ok") or tx.__contains__("yes") or tx.__contains__("got") or tx.__contains__("okay") or tx.__contains__("agree")):
                self.did_accept = True
                final_list.append(button)
        return final_list
