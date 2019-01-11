from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
CHROME_PATH = "/usr/local/bin/chromedriver"


def delay():
    time.sleep(2)

class BaseHeadless:
    driver = None

    def __init__(self):
        options = Options()
        # If we don't want to see chrome in action then uncomment following line
        #options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        self.driver = webdriver.Chrome(CHROME_PATH, chrome_options=options)
        self.driver.set_window_size(1424, 1026)

    def click_elem_by_css(self, css_selector):
        delay()
        self.driver.execute_script(f"return document.querySelector('{css_selector}').click()")

    def set_input_value_by_name(self, name, value):
        field = self.driver.find_element_by_name(name)
        field.clear()
        field.send_keys(value)

    def quit_browser(self):
        if self.driver:
            self.driver.quit()
            self.driver = None
