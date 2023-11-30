import unittest
from selenium import webdriver

class RandaTestTitle(unittest.TestCase):

    def setUp(self):
        self.chromeDriver = webdriver.Chrome()
        self.addCleanup(self.chromeDriver.quit)

    def test_page_title(self):
        self.chromeDriver.get('https://www.randa.ittwoc.com')
        self.assertIn('Laravel', self.chromeDriver.title)

if __name__ == '__main__':
    unittest.main(verbosity=2)