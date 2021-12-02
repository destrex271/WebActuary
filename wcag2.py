import selenium.common.exceptions
from selenium import webdriver
from axe_selenium_python import Axe
from driver_solver import get_driver_path
from directory_create_module import create_dir


class WCAG_TESTER:

    def __init__(self, url):
        self.url = url
        self.folder_name = "wcag2"
        self.tc = 0
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
        driver = webdriver.Chrome(options=op)
        driver.get(f"{self.url}")
        axe = Axe(driver)
        axe.inject()
        results = ""
        try:
            results = axe.run()
        except selenium.common.exceptions.TimeoutException:
            if self.tc <= 3:
                self.validate()
                self.tc += 1
            else:
                return ""
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
                try:
                    fina += "\n" + y[:y.index("Rule")]
                except:
                    fina = ""
            return fina
        return "Problem!"

    def write(self):
        with open(f"{self.folder_name}/wcag_result.txt", "w") as file:
            print("Writing!")
            file.write(self.validate())
            file.close()
            print("Writing Done!")
