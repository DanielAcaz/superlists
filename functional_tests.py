from selenium import webdriver
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
		self.fail('Finish the test!')

		#She is invited to insert one taks item immediately	

		#She types "Buy peacock feathers" inside of a box of table (your hooby is make fly fishing lures)

		#When she enter key, the page is updated. And now, this page show "1: Buy peacock feathers" like an item inside a task list

		#There is still a box inveting her to add other item. She inserts "Use peacock feathers to make a fly". She is methodic 

		#The page is updated again and now show the two itens in your list

		#Edith quenstion herself if the will remember her list. So she sees that site generate an URL just her. There is a litle text explain it.

		#She access this URL and your list still continues there.

		#So, she sleeps now.

if __name__ == '__main__':
	unittest.main(warnings='ignore')
