import scrapy
import os
import requests
from scrapy.crawler import CrawlerProcess
from random import randint
import time
import random
from scrapy.utils.project import get_project_settings


requests.adapters.DEFAULT_RETRIES = 0

print "Folder Selection"
folderSelection = {}

def getUrls():
    with open('./temp_link.txt', 'rb') as file :
        array = []
        for line in file:
            array.append(line)

        random.shuffle(array)
    return array

class QuotesSpider(scrapy.Spider):
    name = "Scrapy Data"

    custom_settings = {
        'DOWNLOAD_DELAY': '3',
        'BOT_NAME': 'Scrapy Data',
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) )'

    }

    def start_requests(self):
        urls = getUrls()
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        # directory = './data_random/'
        directory = './data_average_customer/'
        # directory = './data_featured/'
        # directory = './data_price_high_2_low/'
        # directory = './data_price_low_2_high/'
        # directory = './data_price_newest_arrival/'

        # dir = ['./data_random/',
        #         './data_average_customer/',
        #         './data_featured/',
        #         './data_price_high_2_low/',
        #         './data_price_low_2_high/',
        #         './data_price_newest_arrival/']
        print(response.url.split("&"))
        page = response.url.split("&")[-1]
        filename = 'amazon-%s.html' % page
        with open(os.path.join(directory, filename), 'wb') as f:
            f.write(response.url.strip())
            f.write(response.body)
            print("This prints once a minute.")
            time.sleep(60)


print "Starting Crawl"
## Start crawling process and Spider

count = 1
process = CrawlerProcess()
process.crawl(QuotesSpider)
process.start()
process.stop()





