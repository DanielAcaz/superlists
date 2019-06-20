from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import time


class NewVisitorTest(LiveServerTestCase):

	MAX_WAIT = 10

	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()

	def check_for_row_in_list_table(self, row_text):
		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn(row_text, [row.text for row in rows])

	def test_can_start_a_list_for_one_user(self):
		#Edith heard to speak about a new online app interesting to task lists.
		#She decides to verify this homepage
		self.browser.get(self.live_server_url)

		#She sees that the title of page and your header say 'to-do'
		self.assertIn('To-Do', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text #TO-DO see if is the correct statement find_element_by_tag_name
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
		self.wait_for_row_in_list_table('1: Buy peacock feathers')

		#There is still a box inveting her to add other item. She inserts "Use peacock feathers to make a fly". She is methodic 
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('Use peacock feathers to make a fly')
		inputbox.send_keys(Keys.ENTER)
	
		
		#The page is updated again and now show the two itens in your list
		self.wait_for_row_in_list_table('1: Buy peacock feathers')
		self.wait_for_row_in_list_table('2: Use peacock feathers to make a fly')
		
		#Edith quenstion herself if the will remember her list. So she sees that site generate an URL just her. There is a litle text explain it.

		#She access this URL and your list still continues there.

		#So, she sleeps now.

	def test_multiple_users_can_start_lists_at_diferrent_urls(self):
		#Edith start a new task list
		self.browser.get(self.live_server_url)
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('Buy peacock feathers')
		inputbox.send_keys(Keys.ENTER)
		self.wait_for_row_in_list_table('1: Buy peacock feathers')

		#She seem that your list has a just one url
		edith_list_url = self.browser.current_url
		self.assertRegex(edith_list_url, '/lists/.+')

		#Now, a new user, Francis, arrive in the site

		##We use a new section of the navegator to garantee that anything information of Edith is come from cookie, etc
		self.browser.quit()
		self.browser = webdriver.Firefox()

		#Francis access the home page. There isn't anything sinal of Edith's list
		self.browser.get(self.live_server_url)
		page_text = self.browser.find_element_by_tag_name('body').text
		self.assertNotIn('Buy peacock feathers', page_text)
		self.assertNotIn('make a fly', page_text)

		#Francis start a new list inserting a new item. He is less interesting than Edith...
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('Buy milk')
		inputbox.send_keys(Keys.ENTER)
		self.wait_for_row_in_list_table('1: Buy milk')

		#Francis get your own url exlusive
		francis_list_url = self.browser.current_url
		self.assertRegex(francis_list_url, '/lists/.+')
		self.assertNotEqual(francis_list_url, edith_list_url)

		#Again, there is no sinal about the Edith's list
		page_text = self.browser.find_element_by_tag_name('body').text
		self.assertNotIn('Buy peacock feathers', page_text)
		self.assertIn('Buy milk', page_text)

		#Satisfies, both return to sleep
		self.fail('Finish the test!')


	def wait_for_row_in_list_table(self, row_text): 
		start_time = time.time()
		while True:
			try:
				table = self.browser.find_element_by_id('id_list_table')
				rows = table.find_elements_by_tag_name('tr')
				self.assertIn(row_text, [row.text for row in rows])
				return 
			except (AssertionError, WebDriverException) as e:
				if time.time() - start_time > self.MAX_WAIT:
					raise e
				time.sleep(0.5)
