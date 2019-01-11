import requests
import time
import random
from urllib.parse import urlparse
import logging

######################################SCENARIO##############################################################
# Consider a book library website which offers you to borrow a book but it only offers to authorized users
# and it have a huge collection of books in different categories
###########################################################################################################
#########################STEPS#############################################################################
# - Start a session
# - Perform authorization request (using credentials credentials)
# - Set authorized cookies for future requests
# - Hit fetch book request with categories
# - Get the response and scrap the required data
##########################################################################################################

logger = logging.getLogger(__name__)

LOG_PREFIX = 'RequestManager:'


class RequestManager:
    def __init__(self):
        self.set_user_agents();  # This is to keep user-agent same throught out one request

    crawler_name = None
    session = requests.session()
    # This is for agent spoofing...
    user_agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246',
        'Mozilla/4.0 (X11; Linux x86_64) AppleWebKit/567.36 (KHTML, like Gecko) Chrome/62.0.3239.108 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36',
        'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko',
        'Mozilla/5.0 (compatible, MSIE 11, Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko',
        'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 7.0; InfoPath.3; .NET CLR 3.1.40767; Trident/6.0; en-IN)',
        'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
        'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)',
        'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/5.0)',
        'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/4.0; InfoPath.2; SV1; .NET CLR 2.0.50727; WOW64)',
        'Mozilla/5.0 (compatible; MSIE 10.0; Macintosh; Intel Mac OS X 10_7_3; Trident/6.0)',
        'Mozilla/4.0 (Compatible; MSIE 8.0; Windows NT 5.2; Trident/6.0)',
        'Mozilla/4.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/5.0)',
        'Mozilla/5.0 (X11; Linux i686; rv:64.0) Gecko/20100101 Firefox/64.0',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:64.0) Gecko/20100101 Firefox/64.0',
        'Mozilla/5.0 (X11; Linux i586; rv:63.0) Gecko/20100101 Firefox/63.0',
        'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:63.0) Gecko/20100101 Firefox/63.0',
        'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.10; rv:62.0) Gecko/20100101 Firefox/62.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:10.0) Gecko/20100101 Firefox/62.0',
        'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.13; ko; rv:1.9.1b2) Gecko/20081201 Firefox/60.0',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/58.0.1',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/58.0',
        'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:52.59.12) Gecko/20160044 Firefox/52.59.12',
        'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9a1) Gecko/20060814 Firefox/51.0',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:46.0) Gecko/20120121 Firefox/46.0'
    ]

    headers = {}

    cookie = None
    debug = True

    def file_name(self, context: RequestContext, response, request_type: str = 'GET'):
        url = urlparse(response.url).path.replace("/", "|")
        return f'{time.time()}_{context.get("key")}_{context.get("category")}_{request_type}_{response.status_code}_{url}'

    # write a file, safely
    def write(self, name, text):
        if self.debug:
            file = open(f'logs/{name}.html', 'w')
            file.write(text)
            file.close()

    def set_user_agents(self):
        self.headers.update({
            'user-agent': random.choice(self.user_agents)
        })

    def set_headers(self, headers):
        logger.info(f'{LOG_PREFIX}:SETHEADER set headers {self.headers}')
        self.session.headers.update(headers)

    def get(self, url: str, withCookie: bool = False, context):
        logger.info(f'{LOG_PREFIX}-{self.crawler_name}:GET making get request {url} {context} {withCookie}')
        cookies = self.cookie if withCookie else None
        response = self.session.get(url=url, cookies=cookies, headers=self.headers)
        self.write(self.file_name(context, response), response.text)
        return response

    def post(self, url: str, data, withCookie: bool = False, allow_redirects=True, context: RequestContext = {}):
        logger.info(f'{LOG_PREFIX}:POST making post request {url} {data} {context} {withCookie}')
        cookies = self.cookie if withCookie else None
        response = self.session.post(url=url, data=data, cookies=cookies, allow_redirects=allow_redirects)
        self.write(self.file_name(context, response, request_type='POST'), response.text)
        return response

    def set_cookie(self, cookie):
        self.cookie = cookie
        logger.info(f'{LOG_PREFIX}-{self.crawler_name}:SET_COOKIE set cookie {self.cookie}')

Request = RequestManager()

context = {
    "key": "demo",
    "category": "history"
}
START_URI = "DUMMY_URL" # URL OF SIGNUP PORTAL
LOGIN_API = "DUMMY_LOGIN_API"
response = Request.get(url=START_URI, context=context)

Request.set_cookie('SOME_DUMMY_COOKIE')
Request.set_headers('DUMMY_HEADERS')

response = Request.post(url=LOGIN_API, data = {'username': '', 'passphrase': ''}, context=context)


# HERE YOU CAN DO BOOK FETCH API CALL AS PER SCENARIO DESCRIBE ABOVE