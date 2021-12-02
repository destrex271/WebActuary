import os.path
import shutil
import sys

from ssl_module import SSLModule
from cookie_main_module import CookieModule
from alt_text import AltText
from tab_index import TabIndex
from wcag2 import WCAG_TESTER
import final_report as fin
from directory_create_module import create_dir
from summary_report import get_summary
import PySimpleGUI as sg
import time

import threading

fr = ""
folder = "reports"
'''-------------------------ui goes here-----------------------------------------'''

sg.theme('DarkAmber')  # Add a touch of color
# All the stuff inside your window.
layout = [
    [sg.T(" ", size=(1, 1)), sg.Text('WebActuary - Auditor', auto_size_text=False, justification='center', size=(41, 1),
                                     font=('Arial', 17))],
    [sg.Text(" ")],
    [sg.Text(" ", size=(6, 1)), sg.Text('Enter URL:', ), sg.InputText(),
     sg.FileBrowse(file_types=(("Text Files", "*.txt"),))],
    [sg.T(" ", size=(12, 1)), sg.Checkbox('SSL', default=False, key='-IN1-'), sg.T(" ", size=(3, 1)),
     sg.Checkbox('Cookies', default=False, key='-IN2-'), sg.T(" ", size=(3, 1)),
     sg.Checkbox('ADA', default=False, key='-IN3-'), sg.T(" ", size=(3, 1)),
     sg.Checkbox('ALL', default=False, key='-IN4-')],
    [sg.T()],
    [sg.Text(" ", size=(23, 1)), sg.Button('Audit', size=(7, 1), bind_return_key=True), sg.Text(" ", size=(3, 1)),
     sg.Button('Cancel', size=(7, 1))],

]
# all stuff inside extended window

loading_components = [
    [sg.Text("________________________________________________________________________________")],
    [sg.Text("", size=(30, 1)), sg.T("Auditing...")],
    [sg.T("", size=(18, 1)),
     sg.ProgressBar(max_value=100, orientation='horizontal', size=(20, 15), key='progress_bar')]]
# Create the Window
window = sg.Window('Auditor', resizable=True, transparent_color='red').Layout(layout)

summary = ""
report = ""
url_list = []

ssl_folder = ""
cookie_folder = ""
alt_folder = ""
tab_folder = ""
wcag_folder = ""
only_one = True


def reinit():
    global summary, report, ssl_folder, cookie_folder, alt_folder, tab_folder, wcag_folder
    summary = ""
    ssl_folder = ""
    cookie_folder = ""
    alt_folder = ""
    tab_folder = ""
    wcag_folder = ""


def popup_window():
    global report
    report = f"Report generated at:{os.path.abspath(os.getcwd())}\{folder}"
    if len(url_list) > 1:
        report = report.replace("Report", "Reports")
    analysis = "Analysed"

    layout = [
        [sg.Text("Audit Finished", key="new", auto_size_text=False, justification='center', size=(41, 1),
                 font=('Arial', 17))],
        [sg.T(report, key='report', size=(69, 1))],
        [sg.T(summary, key='summary')],
        [sg.T(" ", size=(28, 1)), sg.Button('OK', size=(7, 1), bind_return_key=True)]
    ]
    window = sg.Window("Second Window", layout, modal=True)
    choice = None

    while True:
        event, values = window.read()

        if event == "OK" or event == sg.WIN_CLOSED:
            break

    window.close()


def remove(trigger_ssl, trigger_cookie, trigger_ada):
    # print(ssl_folder)
    # print(f"{trigger_ssl} {trigger_ada} {trigger_cookie}")
    if trigger_ssl:
        shutil.rmtree(ssl_folder)
    if trigger_cookie:
        declutter(cookie_folder)
    if trigger_ada:
        declutter(alt_folder)
        declutter(tab_folder)
        declutter(wcag_folder)


def ui():
    global only_one
    while True:
        event, values = window.Read(timeout=100)
        if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
            break

        elif event == 'Audit':

            window.extend_layout(window, loading_components)
            url = values[0]
            window.refresh()

            trigger_ssl, trigger_cookie, trigger_ada, trigger_all = False, False, False, False
            if values['-IN1-'] == True:
                trigger_ssl = True
            if values['-IN2-'] == True:
                trigger_cookie = True
            if values['-IN3-'] == True:
                trigger_ada = True
            if values['-IN4-'] == True:
                trigger_all = True
            if trigger_all:
                trigger_ssl, trigger_cookie, trigger_ada = True, True, True

            '''#----------------------thread goes here---------------------------
            # Create a thread from a function with arguments
            th = threading.Thread(target=run_program, args=(url,))

            # Start the thread
            th.start()
            # Wait for thread to finish
            th.join()
            #----------------------thread ends here---------------------------'''

            """if trigger_ssl==True:
                print("ssl")
            if trigger_cookie==True:
                print("cookies")
            if trigger_ada==True:
                print("ada")
            if trigger_all==True:
                print("alll")"""

            if os.path.isfile(url):
                with open(url, "r") as file:
                    li = file.read().split("\n")
                    #print(li)
                    for x in li:
                        url_list.append(x)

                only_one = False
            else:
                url_list.append(url)
            print(f"{url_list}")

            for x in url_list:
                run_program(x, trigger_ssl, trigger_cookie, trigger_ada)
                global summary
                summary += "Summary: " + get_summary(trigger_ssl, trigger_cookie, trigger_ada)
                remove(trigger_ssl, trigger_cookie, trigger_ada)
                print("")
                if not only_one:
                    reinit()
            popup_window()
            sys.exit()

    window.close()


'''------------------ui ends here------------------------------------'''


def run_program(url, trigger_ssl, trigger_cookie, trigger_ada):
    disclaimer = "---------------------DISCLAIMER--------------------- \n\n" + f"This is an automatically generated audit report for the given url: {url}.\n"
    with open("assests/disclaimer.txt", 'r') as file:
        disclaimer += file.read() + "\n"
    st = disclaimer

    if len(url.replace(" ", '')) > 0 and (trigger_ada or trigger_ssl or trigger_cookie or trigger_ada):
        # SSL Module....
        if trigger_ssl:
            ssl_mod = SSLModule(url)
            global ssl_folder
            ssl_folder += ssl_mod.folder_name
            print("Analyzing the security of your website........")
            ssl_mod.get_certificate()
            ssl_text = fin.ssl_report(url)
            # declutter(ssl_mod)
            st += "\n\n---------------------SSL REPORT---------------------\n" + ssl_text + "\n\n"

        # updating loading bar starts
        i = 0
        for i in range(21):
            time.sleep(0.05)
            window['progress_bar'].update_bar(i)

        # updating loading bar ends
        window.refresh()

        # Cookies Module......."""
        if trigger_cookie:
            cookie_mod = CookieModule(url)
            global cookie_folder
            cookie_folder += cookie_mod.folder_name
            print("Checking For Cookie/Privacy policy........")
            cookie_mod.gen_all_json()
            cookie_mod.conv_to_json()
            cookie_mod.cat_acc_domain()
            ck_report = fin.total_cookie_report()
            consent_report = fin.cookie_consent()
            st += "\n---------------------COOKIE REPORT---------------------\n" + ck_report + consent_report + "\n\n"

            # declutter(cookie_mod)

        # updating loading bar starts
        window.refresh()
        for i in range(22, 43):
            time.sleep(0.05)
            window['progress_bar'].update_bar(i)

        # updating loading bar ends
        window.refresh()
        # Alt Index
        if trigger_ada:
            alt_text_mod = AltText(url)
            global alt_folder
            alt_folder += alt_text_mod.folder_name
            tab_index_mod = TabIndex(url)
            global tab_folder
            tab_folder += tab_index_mod.folder_name
            w_mod = WCAG_TESTER(url)
            global wcag_folder
            wcag_folder += w_mod.folder_name
            print("\nChecking for accesibility Issues..........")
            alt_text_mod.alt_check()
            print("Alternate Text report generated!")

            # updating loading bar starts
            window.refresh()
            for i in range(44, 68):
                time.sleep(0.05)
                window['progress_bar'].update_bar(i)

            # updating loading bar ends
            window.refresh()

            # Tab Index
            tab_index_mod.tab_index_check()
            print("Tabbed Text Report generated!")

            # updating loading bar starts
            window.refresh()
            for i in range(69, 74):
                time.sleep(0.05)
                window['progress_bar'].update_bar(i)

            # updating loading bar ends
            window.refresh()
            # WCAG!
            w_mod.write()
            print("Color Contrast Ratio Report generated !")

            # updating loading bar starts
            window.refresh()
            for i in range(75, 89):
                time.sleep(0.05)
                window['progress_bar'].update_bar(i)

            # updating loading bar ends
            window.refresh()
            alt_report = fin.alt_img()
            contrast_report = fin.color_contrast()
            if len(alt_report.replace(" ", '')) == 0:
                alt_report = "No Violations were discovered in case of Image accessibility!"
            tab_report = fin.tab_index()
            if len(tab_report.replace(" ", '')) == 0:
                tab_report = "Your website has a proper tab navigation!"
            if len(contrast_report.replace(" ", '')) == 0:
                contrast_report = "No violations were discovered in case of Contrast Ratios as per the W3C Guidelines!"
            """declutter(alt_text_mod)
            declutter(tab_index_mod)
            declutter(w_mod)"""
            st += "\n\n---------------------ALT TEXT---------------------\n\n" + alt_report + "\n\n---------------------TAB NAVIGATION---------------------\n\n" + tab_report + "\n\n---------------------COLOR CONTRAST---------------------\n\n" + contrast_report + "\n\n"
        # time.sleep(10)
        fr = f"final_report_({fin.format_link(url)}).txt"
        create_dir(f"{folder}")
        with open(f'{folder}/{fr}', 'w', errors="ignore") as file:
            file.write(st)
            file.close()
        # updating loading bar starts
        window.refresh()
        for i in range(90, 91):
            time.sleep(0.05)
            window['progress_bar'].update_bar(i)

        # updating loading bar ends
        window.refresh()

        print("Decluttering.....")

        print(f"Final Report generated as a text file at {os.path.abspath(os.getcwd())}\{folder} with the name: {fr}")

        # updating loading bar starts
        window.refresh()
        for i in range(92, 101):
            time.sleep(0.05)
            window['progress_bar'].update_bar(i)

        # updating loading bar ends
        window.refresh()
        return True
    else:
        global summary
        summary = "No url Was Given!"
        global report
        report = ""
        window.close()
        sys.exit(0)


def declutter(folder):
    shutil.rmtree(folder)


if __name__ == "__main__":
    print("\t\t\t-----------------------")
    print("\t\t\t Welcome to WebActuary ")
    print("\t\t\t-----------------------")
    ui()
