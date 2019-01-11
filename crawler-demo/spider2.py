import requests
from parsel import Selector

import time
start = time.time()

### Crawling to the website fetch links and images -> store images -> crawl more to the fetched links and scrap more images
all_images  = {} # website links as "keys" and images link as "values"
# GET request to recurship site
response = requests.get('http://recurship.com/')
selector = Selector(response.text)
href_links = selector.xpath('//a/@href').getall()
image_links = selector.xpath('//img/@src').getall()

for link in href_links:
    try:
        response = requests.get(link)
        if response.status_code == 200:
            image_links = selector.xpath('//img/@src').getall()
            all_images[link] = image_links
    except Exception as exp:
        print('Error navigating to link : ', link)





print(all_images)
end = time.time()
print("Time taken in seconds : ", (end-start))