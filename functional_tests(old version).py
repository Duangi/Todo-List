from selenium import webdriver
import unittest
    
class NewVisitorTest(unittest.TestCase):#(1)

    def setUp(self):#(3)
        self.browser=webdriver.Firefox()

    def tearDown(self):#(3)
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a cool new online to-do app.She goes
        # to chech out its homepage
        self.browser.get('http://localhost:8000')
        
        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do',self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do',header_text)
        
        # She is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
            )
        # She types "Buy peacock fathers"into a text box(Edith's hobby
        # is tying fly-fishing lures)
        inputbox.send_keys('Buy peacock feathers')
        
        # when she hits enter,the page updates ,and now thr page lists
        # "1:Buy peacock feathers to make a fly"(Edith is very methodical)
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1:Buy peacock feathers' for row in rows)
            )
        # There is still a text box inviting her to add another item.She
        # enters "Use peacock feathers to make a fly"(Edith is very methodical)
        self.fail('Finish the test!')
# The page updates again,and now shows both items on her list

# Edith wonders whether the site will remember her list.Then she sees
# that the site has generated a unique URL for her --there is some
# explanatory text to that effect

# She visits that URL - her to-do list is still there.

# Satisfied,she goes back to sleep
