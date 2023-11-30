import unittest
from selenium import webdriver

class RandaTestTitle(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.addCleanup(self.browser.quit)

    def test_page_title(self):
        self.browser.get('https://www.randa.ittwoc.com')
        self.assertIn('Laravel', self.browser.title)

if __name__ == '__main__':
    unittest.main(verbosity=2)