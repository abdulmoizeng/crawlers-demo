from headless.base import BaseHeadless
from headless.creds import CREDS


class GithubHeadlessPage(BaseHeadless):
	uri = "https://github.com/login"

	def login(self):
		self.driver.get(self.uri)
        # Step1 :  Filling login form
		self.set_input_value_by_name(
			"login", CREDS["username"])
		self.set_input_value_by_name(
			"password", CREDS["password"])
        # Step2 :  Submitting login form
		self.click_elem_by_css('[name="commit"]')

	def move_around(self):
		self.driver.get("https://github.com/abdulmoizeng/python-baby-steps")
		self.click_elem_by_css('.starred > button')


	def logout(self):
		self.click_elem_by_css('.HeaderNavlink.mt-1')
		self.click_elem_by_css('.dropdown-signout')
		#dropdown - signout