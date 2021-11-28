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


import PySimpleGUI as sg
import time

fr = ""
folder = "reports"

'''-----------------------ui goes here---------------------------'''

sg.theme('DarkAmber')  # Add a touch of color
# All the stuff inside your window.
layout = [[sg.Text('WebActuary - Auditor', justification='center', size=(41, 1), auto_size_text=True,
                   font=('Arial', 17))],
          [sg.Text(" ")],
          [sg.Text(" ", size=(6, 1)), sg.Text('Enter URL:', ), sg.InputText()],
          [sg.Text("")],
          [sg.Text(" ", size=(21, 1)), sg.Button('Audit', size=(7, 1)), sg.Text(" ", size=(1, 1)),
           sg.Button('Cancel', size=(7, 1))]

          ]
# all stuff inside extended window
loading_components = [
    [sg.Text("____________________________________________________________________________")],
    [sg.Text("", size=(27, 1)), sg.T("Auditing...")],
    [sg.T("", size=(15, 1)),
     sg.ProgressBar(max_value=100, orientation='horizontal', size=(20, 15), key='progress_bar')]]
# Create the Window
window = sg.Window('Auditor', resizable=True).Layout(layout)

def ui():
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
            break
        elif event == 'Audit':

            window.extend_layout(window, loading_components)
            url = values[0]
            window.refresh()
            run_program(url)
            sg.popup(f"Report generated at:\n {os.path.abspath(os.getcwd())}\{folder} ",font=("Arial",11))
            sys.exit()


    window.close()

'''------------------ui ends here------------------------------------'''



def run_program(url):
    ssl_mod = SSLModule(url)
    cookie_mod = CookieModule(url)
    alt_text_mod = AltText(url)
    tab_index_mod = TabIndex(url)
    w_mod = WCAG_TESTER(url)

    # SSL Module....
    print("Analyzing the security of your website........")
    ssl_mod.get_certificate()

    #updating loading bar starts
    i = 0
    for i in range(21):
        time.sleep(0.05)
        window['progress_bar'].update_bar(i)

    #updating loading bar ends


    # Cookies Module......."""
    print("Checking For Cookie/Privacy policy........")
    cookie_mod.gen_all_json()
    cookie_mod.conv_to_json()
    cookie_mod.cat_acc_domain()

    # updating loading bar starts
    window.refresh()
    for i in range(22,43):
        time.sleep(0.05)
        window['progress_bar'].update_bar(i)

    # updating loading bar ends

    # Alt Index
    print("\nChecking for accesibility Issues..........")
    alt_text_mod.alt_check()
    print("Alternate Text report generated!")

    # updating loading bar starts
    window.refresh()
    for i in range(44,68):
        time.sleep(0.05)
        window['progress_bar'].update_bar(i)

    # updating loading bar ends

    # Tab Index
    tab_index_mod.tab_index_check()
    print("Tabbed Text Report generated!")

    # updating loading bar starts
    window.refresh()
    for i in range(69,74):
        time.sleep(0.05)
        window['progress_bar'].update_bar(i)

    # updating loading bar ends

    # WCAG!
    w_mod.write()
    print("Color Contrast Ratio Report generated !")

    # updating loading bar starts
    window.refresh()
    for i in range(75,89):
        time.sleep(0.05)
        window['progress_bar'].update_bar(i)

    # updating loading bar ends

    # time.sleep(10)
    fr = f"final_report_({fin.format_link(url)}).txt"
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
    create_dir(f"{folder}")
    with open(f'{folder}/{fr}', 'w') as file:
        st = disclaimer + "\n\n---------------------SSL REPORT---------------------\n" + ssl_text + "\n---------------------COOKIE REPORT---------------------\n" + ck_report + consent_report + "\n\n---------------------ALT TEXT---------------------\n\n" + alt_report + "\n\n---------------------TAB NAVIGATION---------------------\n\n" + tab_report + "\n\n---------------------COLOR CONTRAST---------------------\n\n" + contrast_report + "\n\n"
        file.write(st)

     # updating loading bar starts
    window.refresh()
    for i in range(90,91):
        time.sleep(0.05)
        window['progress_bar'].update_bar(i)

     # updating loading bar ends

    print("Decluttering.....")
    declutter(ssl_mod)
    declutter(cookie_mod)
    declutter(alt_text_mod)
    declutter(tab_index_mod)
    declutter(w_mod)
    print(f"Final Report generated as a text file at {os.path.abspath(os.getcwd())}\{folder} with the name: {fr}")

    # updating loading bar starts
    window.refresh()
    for i in range(92,101):
        time.sleep(0.05)
        window['progress_bar'].update_bar(i)

    # updating loading bar ends

    return True


def declutter(mod):
    shutil.rmtree(mod.folder_name)


if __name__ == "__main__":
    print("\t\t\t-----------------------")
    print("\t\t\t Welcome to WebActuary ")
    print("\t\t\t-----------------------")
    ui()