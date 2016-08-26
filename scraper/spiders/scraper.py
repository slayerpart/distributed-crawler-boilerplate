from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.http import Request
from bs4 import BeautifulSoup as bs
from linkexplorer.items import ExampleItem

class ExampleSpider(Spider):
    # In each callback you should ensure that the proxy really returned your desired webpage
    # by checking for some invariant property, such as:
    # if not hxs.select('//get/site/logo'):
    #   yield Request(url=response.url, dont_filter=True)
    name = "scraper"
    database = "default" # name of MongoDB database
    collection = "default" # name of MongoDB's DB collection

    def parse(self, response):
        pass
