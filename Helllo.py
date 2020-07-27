import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class Helllo(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path= r"C://Users/tensi/OneDrive/Escritorio/Platzi/py/Ex/Ex2/chromedriver.exe")
        driver = self.driver
        driver.implicitly_wait(10)

    def test_helllo(self):
        driver = self.driver
        driver.get('https://www.platzi.com')

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output='reportes', report_name='hello-world-report'))