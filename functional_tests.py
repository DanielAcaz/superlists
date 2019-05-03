from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest


class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):
		#Edith heard to speak about a new online app interesting to task lists.
		#She decides to verify this homepage
		self.browser.get("http://localhost:8000")

		#She sees that the title of page and your header say 'to-do'
		self.assertIn('To-Do', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do', header_text)

		#She is invited to insert one taks item immediately	
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(
			inputbox.get_attribute('placeholder'),
			'Enter a to-do item'
		)

		#She types "Buy peacock feathers" inside of a box of table (your hooby is make fly fishing lures)
		inputbox.send_keys('Buy peacock feathers')
		#When she enter key, the page is updated. And now, this page show "1: Buy peacock feathers" like an item inside a task list
		inputbox.send_keys(Keys.ENTER)
		time.sleep(1)

		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertTrue(
			any(row.text == '1: Buy peacock feathers' for row in rows), f"New to-do item did not appear in table. Contents were: \n{table.text}"
		)
		#There is still a box inveting her to add other item. She inserts "Use peacock feathers to make a fly". She is methodic 

		#The page is updated again and now show the two itens in your list

		#Edith quenstion herself if the will remember her list. So she sees that site generate an URL just her. There is a litle text explain it.

		#She access this URL and your list still continues there.

		#So, she sleeps now.
		self.fail('Finish the test!')

if __name__ == '__main__':
	unittest.main(warnings='ignore')
