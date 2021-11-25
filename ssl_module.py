import ssl
from directory_create_module import create_dir
from ssl import SSLError
import json


class SSLModule:

    def __init__(self, url_arg):

        """
        This is the constructor for our class
        :param url_arg:
        """
        self.url = url_arg
        self.ls = 0
        self.folder_name = "ssl_certificates"
        self.port = "443"
        self.server_add = (self.format_link(), self.port)

        create_dir(f"{self.folder_name}")

    def format_link(self):

        """
        This function aims at extracting the domain name of the webiste.
        :return:
        """

        link = self.url[self.url.index("//") + 2:]
        server_name = link[:link.index("/")]
        return server_name

    def get_certificate(self):

        """
        To get the raw ssl certificate of the website
        :return:
        """

        tx = ""

        try:
            encrypted_ssl_cert = ssl.get_server_certificate(addr=self.server_add)
            self.write_to_file("cert.pem", encrypted_ssl_cert)
            self.conv_to_json("cert.pem")
        except ssl.SSLEOFError:
            tx = "Your Website possess a Valid ssl Certificate but we are not able to analyze it !"
            self.write_to_file("ssl.txt", tx)
            self.write_to_file("ssl.json", tx)
        except SSLError:
            tx = "Your website does not possess a valid SSL Certificate"
            self.write_to_file("ssl.txt", tx)
            self.write_to_file("ssl.json", tx)
        except ConnectionResetError:
            tx = "Your website does not possess a valid SSL Certificate"
            self.write_to_file("ssl.txt", tx)
            self.write_to_file("ssl.json", tx)
        except ConnectionError:
            if self.ls <= 3:
                self.get_certificate()
                self.ls += 1
        else:
            tx = "SSL Certificate Analyzed!"
        print(tx)

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

    def conv_to_json(self, file):
        ordered_dict = ssl._ssl._test_decode_cert(f"{self.folder_name}/{file}")
        json_obj = json.dumps(ordered_dict)
        self.write_to_file("ssl.json", json_obj)
