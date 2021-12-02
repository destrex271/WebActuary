import json
import os
from datetime import datetime
from final_report import cookie_consent


def ssl_summary():
    ssl_dict = {}
    link = "https://www.globalsign.com/en/ssl-information-center/what-is-an-ssl-certificate"

    with open('ssl_certificates/ssl.json', 'r') as file:
        try:
            ssl_dict = json.load(file)
            expiry = ssl_dict['notAfter']
            expiry_datetime = datetime.strptime(expiry, r'%b %d %H:%M:%S %Y %Z')
            today_datetime = datetime.now().utcnow()
            dif_time = expiry_datetime - today_datetime
            days = dif_time.days
            #print(days)
            tx = "\nYour Website has a valid SSL certificate!"
            if int(str(days)) <= 100:
                tx += f"\nBut your certificate will soon expire in {dif_time.days} days!"
            return tx
        except json.decoder.JSONDecodeError:
            x = open("ssl_certificates/ssl.txt", "r").read()
            if not x == "Your Website possess a Valid ssl Certificate but we are not able to analyze it !":
                x += f"\nIF YOUR WEBSITE DOES NOT POSSESS AN SSL CERTIFICATE PLEASE CHECK OUT THIS DOCUMENTATION FOR MORE INFORMATION : {link}"
            else:
                x += "\n"
            return "\n" + x


def cookie_summary():
    tx = ""
    cookie_dict = {}
    # Count cookie....
    if os.path.isfile('cookies/cookies.json'):
        with open('cookies/cookies.json') as file:
            cookie_dict = json.load(file)
        print(cookie_dict)
        tx = f"\nTotal Cookies detected were : {len(cookie_dict)}"
    else:
        tx = "\nNo Cookies were detected!"
    # .................

    # Consent and link
    consent = cookie_consent()
    tx += f"{consent}"
    return tx


def alt_summary():
    tx = ""
    with open("alt_text/alt_text.txt", 'r') as file:
        mx = file.read()
        print(mx)
        mx = str(mx)
        if len(mx.strip()) > 0:
            tx = "\nYour Webpage has some images that do not have an alternate text associated with them!"
        else:
            tx = "\nYay! No violations were detected regarding alternate text in your images."

        return tx


def tab_summary():
    link = "https://webaim.org/techniques/keyboard/tabindex"
    with open("tab_index/tab_index.txt", 'r', encoding="utf-8") as file:
        mx = file.read()
        mx = str(mx)
        if len(mx) > 0:
            tx = f"\nYour Website isn't tab indexed properly.\nYou are requested to use the global attribute 'tabindex' in <a> <button> <input> and other such elements that you might consider essential for navigation via a Keyboard on your website!\n Please take a look at {link} for more information!"
        else:
            tx = "\nHooray! Your website is tab indexed properly."
    return tx


def wcag_summary():
    tx = ""
    link = "https://www.w3.org/TR/UNDERSTANDING-WCAG20/visual-audio-contrast-contrast.html"
    with open("wcag2/wcag_result.txt", "r") as file:
        mx = file.read()
        if len(mx.strip()) > 0:
            tx += f"\nYour Webpage violates the W3C.org guidelines regarding color contrast ratios.\nYou are requested to check {link} to fix this"
        else:
            tx += "\nWoHoo! Your webpages does not violate any of the color contrast ratio guidelines given by W3C.org"

    return tx


def get_summary(t_ssl, t_cookie, t_ada):
    tx = ""
    if t_ssl:
        tx += ssl_summary() + "\n"
    if t_cookie:
        tx += cookie_summary() + "\n"
    if t_ada:
        tx += alt_summary() + "\n" + tab_summary() + "\n" + wcag_summary() + "\n"
    return tx
