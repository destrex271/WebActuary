from selenium import webdriver
from axe_selenium_python import Axe
from directory_create_module import create_dir


class WCAG_TESTER:

    def __init__(self, url):
        self.url = url
        self.folder_name = "wcag2"
        create_dir(self.folder_name)

    def find_all(self, a_str, sub):
        start = 0
        while True:
            start = a_str.find(sub, start)
            if start == -1: return
            yield start
            start += len(sub)

    def validate(self):
        op = webdriver.ChromeOptions()
        op.add_argument("--log-level=3")
        op.add_argument("--headless")
        driver = webdriver.Chrome(executable_path='drivers/chromedriver_win32/chromedriver.exe', options=op)
        driver.get(f"{self.url}")
        axe = Axe(driver)
        axe.inject()
        results = axe.run()
        axe.write_results(results, 'a11y.json')
        driver.close()

        try:
            assert len(results["violations"]) == 0, axe.report(results["violations"])
        except AssertionError as e:
            t = str(e)
            m = list(self.find_all(t, 'color-contrast '))
            fina = ""
            for i in m:
                y = t[i:]
                fina += "\n" + y[:y.index("Rule")]
            return fina
        return "Problem!"

    def write(self):
        with open(f"{self.folder_name}/wcag_result.txt", "w") as file:
            print("Writing!")
            file.write(self.validate())
            file.close()
            print("Writing Done!")
