import unittest
from selenium import webdriver


class NewVisitorTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(5)

    def testCan(self):
        #Effie has heard about a new cool online to-do app. She goes 
        #online to check out its homepage
        self.browser.get('http://localhost:8000')

        #She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish test')

        #She is invited to enter a to do item straight away

        #She types "Buy peacock feathers" into a text box (Effie's 
        #hobby is fighting peacock feathers)

        #When she hits enter the page updates, and now the page lists 
        #"1. Buy peacock feathers" as an item in a to do list

        #There is still a text box inviting her to add another item. 
        #She enters "Use peacock feathers to make a fly"

        #The page updates again, and now shows both items on her to
        #do list.

        #Edith wonders if the page will remember her to do list and
        #then notices that the site has generated a unique url for her
        #-----there is also so explanatory text to that effect.

        #She visits the url and finds her to do list  is still there

        #Satisfied she goes back to sleep
	
    def tearDown(self):
        self.browser.quit()

if __name__ == '__main__':
        unittest.main()

