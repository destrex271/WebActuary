import datetime
from datetime import timezone
import json

# --------------------------------------- SSL REPORT GENERATOR ------------------------------------------------------
import os.path


def format_issuer(issuer):
    x = ""
    cnt = 0
    i = 0
    li = 0
    for ie in issuer:
        if ie == ',':
            cnt += 1
        if cnt == 2:
            y = issuer[li + 1:i]
            x += "\r" + "\t" + y.replace(",", " : ").strip()
            cnt = 0
            li = i
        i += 1
    return x.replace("Name", " name")


def format_link(url):
    """
    This function aims at extracting the domain name of the webiste.
    :return:
    """

    link = url[url.index("//") + 2:]
    server_name = link[:link.index("/")]
    return server_name


def ssl_report(url):
    ssl_dict = {}
    ssl_text = ""
    link = "https://www.globalsign.com/en/ssl-information-center/what-is-an-ssl-certificate"
    with open('ssl_certificates/ssl.json', 'r') as file:
        try:
            ssl_dict = json.load(file)
        except json.decoder.JSONDecodeError:
            x = open("ssl_certificates/ssl.txt", "r").read()
            if not x == "Your Website possess a Valid ssl Certificate but we are not able to analyze it !":
                x += f"\n\nIF YOUR WEBSITE DOES NOT POSSESS AN SSL CERTIFICATE PLEASE CHECK OUT THIS DOCUMENTATION FOR MORE INFORMATION : {link}\n\n"
            else:
                x += "\n"
            return "\n" + x
    issuer = " " + str(ssl_dict['issuer']).replace('[', " ").replace(']', ' ').strip().replace("'", '') + ","
    x = format_issuer(issuer)
    ssl_text += f"\nIssued To - {format_link(f'{url}')}\n"
    ssl_text += f"\nIssued by :\n {x}\n"
    ssl_text += f"\nValid From : {str(ssl_dict['notBefore']).replace('GMT', 'UTC')}\nValid Upto : {str(ssl_dict['notAfter']).replace('GMT', 'UTC')}\n"

    return ssl_text


# -------------------------------------------------------------------------------------------------------------

# -------------------------------------- COOKIES REPORT -------------------------------------------------------

def total_cookie_report():
    cookie_dict = {}
    total_cookie_text = ""

    if os.path.isfile('cookies/cookies.json'):

        total_cookie_text += "\nCOOKIES DETECTED : \n"
        domain = ""
        expiry = ""
        value = ""
        sec_text = ""

        with open('cookies/cookies.json') as file:
            cookie_dict = json.load(file)
        for ck in cookie_dict:
            print("\t")
            if ('secure' in ck) and ck['secure']:
                sec_text = "Send For : For Secure Connections Only!"
            else:
                sec_text = "Send For : For All Connections"
            if 'domain' in ck:
                domain = f"Domain : {ck['domain']}"
            if 'expiry' in ck:
                expiry = f"Expires On : {datetime.datetime.fromtimestamp(ck['expiry']).utcnow()} UTC"
            if 'value' in ck:
                value = f"Value : {ck['value']}"

            total_cookie_text += f"\n\t{domain}\n\t\t{expiry}\n\t\t{value}\n\t\t{sec_text}"
        total_cookie_text += "\n"
    else:
        total_cookie_text += "No Cookies are being used website!"
    return total_cookie_text


# -------------------------------------------------------------------------------------------------------------

# ----------------------------- COOKIE CONSENT REPORT ---------------------------------------------------------

def cookie_consent():
    consent = ""

    if os.path.isfile('cookies/cookie_consent.json'):
        with open('cookies/cookie_consent.json') as file:
            cookie_dict = json.load(file)
            p_link = cookie_dict['policy_link']
            if p_link.__contains__('http'):
                consent += f"\n\nPolicy Link : {p_link}"
                if cookie_dict['did_accept']:
                    consent += "\nUser's Consent was taken!"
                else:
                    consent += "\nAlthough the policy is mentioned but the user's Consent was not taken!"
            elif len(p_link) == 0 and not cookie_dict['total_cookies'] == 0:
                consent += "\nNeither a policy is mentioned nor the user's consent was taken!\n\nYOU ARE ADVISED TO DRAFT A COOKIE/PRIVACY POLICY FOR YOUR WEBSITE AND PROVIDE AN OPTION TO THE USERS TO GIVE THEIR CONSENT FOR THE USAGE OF THESE COOKIES!"

    return consent


# -----------------------------------------------------------------------------------------------------------

# --------------------------------------------- ALT IMAGE ---------------------------------------------------

def alt_img():
    tx = ""
    link = "https://webaim.org/techniques/alttext/"
    with open("alt_text/alt_text.txt", 'rb') as file:
        mx = file.read().decode('utf-8')
        mx = str(mx)
        if len(mx.strip()) > 0:
            tx = f"The Following <img> tags do not have an 'alt-text' attribute as in accordance with ADA Compliance Guidelines : \n\n" + mx + f"\n\nYOU ARE SUGGESTED TO ADD THE 'alt' ATTRIBUTE TO THESE ELEMENTS TO IMPROVE THE ACCESSIBILITY OF YOUR WEBSITE!\nPLEASE TAKE A LOOK AT THIS RESOURCE TO SOLVE YOUR PROBLEM :\n{link} "
    return tx


# -----------------------------------------------------------------------------------------------------------

# -------------------------------------------- TAB INDEX ----------------------------------------------------

def tab_index():
    tx = ""
    link = "https://webaim.org/techniques/keyboard/tabindex"
    with open("tab_index/tab_index.txt", 'rb') as file:
        mx = file.read().decode('utf-8')
        mx = str(mx)
        if len(mx.strip()) > 0:
            tx = f"Your Website isn't tab indexed properly.\nYou are requested to use the global attribute 'tabindex' in <a> <button> <input> and other such elements that you might consider essential for navigation via a Keyboard on your website!\n Please take a look at {link} for more information!"
    return tx


# -------------------------------------------------------------------------------------------------------------

def color_contrast():
    tx = ""
    link = "https://www.w3.org/TR/UNDERSTANDING-WCAG20/visual-audio-contrast-contrast.html"
    with open("wcag2/wcag_result.txt", "r") as file:
        mx = file.read()
        if len(mx.strip()) > 0:
            tx = "The following elements have insufficient color contrast. Please take a look at the list \n\n" + mx.strip() + f"\n\nWe request you to please check out this documentation({link}) to fix these issues with your websites!"
    return tx
