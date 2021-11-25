# Web Crawler #
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
  'dependencies.bat' file can be used to install all the libraries required for this tool to work.
  
  'begin_audit.bat' file is the main file that can be used to run this tool.
  
  ![Running bat](https://i.imgur.com/u8HcruS.png)
  ![Finished bat](https://i.imgur.com/fIGHkb4.png)
  __Both these files are present in the windows folder__


