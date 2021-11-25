import platform


def get_driver_path():
    os_name = platform.system()

    if os_name == "Windows":
        return 'drivers/windows/chromedriver.exe'
    elif os_name == "Linux":
        return 'drivers/linux/chromedriver'
    elif os_name == "Darwin":
        return 'drivers/mac/chromedriver'
