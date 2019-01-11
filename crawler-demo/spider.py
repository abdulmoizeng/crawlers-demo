import requests
from parsel import Selector

import time
start = time.time()

### Crawling to the website

# GET request to recurship site
response = requests.get('http://recurship.com/')

## Setup for scrapping tool

# "response.txt" contain all web page content
selector = Selector(response.text)

# Extracting href attribute from anchor tag <a href="*">
href_links = selector.xpath('//a/@href').getall()


#Extracting src attribute from img tag <img src="*">
image_links = selector.xpath('//img/@src').getall()

print('*****************************href_links************************************')
print(href_links)
print('*****************************/href_links************************************')



print('*****************************image_links************************************')
print(image_links)
print('*****************************/image_links************************************')



end = time.time()
print("Time taken in seconds : ", (end-start))