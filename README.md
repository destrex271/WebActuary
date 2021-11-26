# Web Actuary #
### A simple console tool to check the accessibility issues of your website ###

This tool prepares a report based for the given url based of on these parameters:

- Details of the SSL Certificate
- Cookies being used (only session cookies)
- ADA Compliance Violations

  - Alt text in all images
  - Color Contrast as per w3.org
  - Tabbed Navigation in a website

## Dependencies ##

Chrome Web Browser is an absolute requirement for this tool to work properly.

Python Version 3.3+ is required for this tool.

Chrome Web Driver:

Download the Chrome webdriver for your specific operating system and follow the steps accordingly.

- Windows
  - Create a directory name `C:\bin`
  - Check your chrome browser version from `Menu>Help>About Chrome` from google chrome browser.(it would be a number like 96.0.445.0 etc)
  - Download the chrome driver according to your chrome version from `https://chromedriver.chromium.org/downloads`
  - Extract the zip file and copy the chromedriver.exe file to `C:\bin`
  - Setup the Environment variable for the chromewebdriver as follows:
    - 
    - Search for 'Env' in start launcher and click on 'Edit the System environment variables' option.
    
      !['Control Panel'](https://i.imgur.com/zE1TUF0.png)
      -
      - Open the Environment variables window.

      !['Env App'](https://i.imgur.com/6TzjjYH.png)
      
      - Edit the Path variable in User variables and add C:\bin to it
      !['Add to Path'](https://i.imgur.com/z2kJyvR.png)
  - Verify setup with `chromedriver.exe -v` and check if the version mentions your google chrome version.
- Linux
  - Please check your google chrome version by running `google-chrome --version` in your terminal.
  - Download the chrome webdriver according to the chrome version from `https://chromedriver.chromium.org/downloads`
  - Unzip the folder and copy the `chromedriver` file to `/usr/bin/chromedriver` by `sudo mv chromedriver /usr/bin/chromedriver`
  - Run these commands to make it executable `sudo chown root:root /usr/bin/chromedriver` and `sudo chmod +x /usr/bin/chromedriver`

The python libraries required for this tool are:

    requests
    selenium
    axe_selenium_python
    bs4 ( BeautifulSoup )
    pyqt5
    PyQtWebEngine
    validators

___You Can install these dependencies manually using pip or you can use the dependency scripts as mentioned below.___

## Running this tool on various operating systems ##

- ### Windows ###
  Navigate to the `windows` folder under `WebActuary-main/` and run the `dependencies.py` file in order to get all the libraries being used.
  
  After this run the `begin_audit.bat` file to start the applications.

  'dependencies.bat' file can be used to install all the libraries required for this tool to work.
  
  'begin_audit.bat' file is the main file that can be used to run this tool.
  
  ![Running bat](https://i.imgur.com/u8HcruS.png)
  ![Finished bat](https://i.imgur.com/fIGHkb4.png)



## Known Issues ##
- Please ensure that your python installation has the python3.dll file along with it. If not you might face an error similar to this:

      from PyQt5.QtWebEngineWidgets import QWebEnginePage
      ImportError: DLL load failed while importing QtWebEngineWidgets: The specified module could not be found.

- For an accurate audit report kindly disable chrome extensions like darkreader that might affect the default User Interface of the webpage since most of the accessibility tests are run on the client side.
 
- Also kindly disable other chrome extensions that might block the cookies and pop-ups/banners.
- If you face an error like:
      This version of ChromeDriver only supports Chrome version X.
      Please download the suitable driver from https://chromedriver.chromium.org/downloads according to the version as seen in the error according to your operating system.
