import os.path
import shutil
from ssl_module import SSLModule
from cookie_main_module import CookieModule
from alt_text import AltText
from tab_index import TabIndex
from wcag2 import WCAG_TESTER
import final_report as fin

fr = "final_report.txt"


def run_program(url):
    ssl_mod = SSLModule(url)
    cookie_mod = CookieModule(url)
    alt_text_mod = AltText(url)
    tab_index_mod = TabIndex(url)
    w_mod = WCAG_TESTER(url)

    # SSL Module....
    print("Analyzing the security of your website........")
    ssl_mod.get_certificate()

    # Cookies Module......."""
    print("Checking For Cookie/Privacy policy........")
    cookie_mod.gen_all_json()
    cookie_mod.conv_to_json()
    cookie_mod.cat_acc_domain()

    # Alt Index
    print("\nChecking for accesibility Issues..........")
    alt_text_mod.alt_check()
    print("Alternate Text report generated!")

    # Tab Index
    tab_index_mod.tab_index_check()
    print("Tabbed Text Report generated!")

    # WCAG!
    w_mod.write()
    print("Color Contrast Ratio Report generated !")

    # time.sleep(10)
    disclaimer = "---------------------DISCLAIMER--------------------- \n\n" + f"This is an automatically generated audit report for the given url: {url}.\n"
    with open("assests/disclaimer.txt", 'r') as file:
        disclaimer += file.read() + "\n"
    ssl_text = fin.ssl_report(url)
    ck_report = fin.total_cookie_report()
    consent_report = fin.cookie_consent()
    alt_report = fin.alt_img()
    contrast_report = fin.color_contrast()
    if len(alt_report.replace(" ", '')) == 0:
        alt_report = "No Violations were discovered in case of Image accessibility!"
    tab_report = fin.tab_index()
    if len(tab_report.replace(" ", '')) == 0:
        tab_report = "Your website has a proper tab navigation!"
    if len(contrast_report.replace(" ", '')) == 0:
        contrast_report = "No violations were discovered in case of Contrast Ratios as per the W3C Guidelines!"
    with open(f'{fr}', 'w') as file:
        st = disclaimer + "\n\n---------------------SSL REPORT---------------------\n" + ssl_text + "\n---------------------COOKIE REPORT---------------------\n" + ck_report + consent_report + "\n\n---------------------ALT TEXT---------------------\n\n" + alt_report + "\n\n---------------------TAB NAVIGATION---------------------\n\n" + tab_report + "\n\n---------------------COLOR CONTRAST---------------------\n\n" + contrast_report + "\n\n"
        file.write(st)
    print("Decluttering.....")
    declutter(ssl_mod)
    declutter(cookie_mod)
    declutter(alt_text_mod)
    declutter(tab_index_mod)
    declutter(w_mod)
    print(f"Final Report generated as a text file at {os.path.abspath(os.getcwd())} with the name: {fr}")


def declutter(mod):
    shutil.rmtree(mod.folder_name)


if __name__ == "__main__":
    print("\t\t-----------------------")
    print("\t\t Welcome to WebActuary ")
    print("\t\t-----------------------")
    run_program(input("Enter Url to audit > "))
