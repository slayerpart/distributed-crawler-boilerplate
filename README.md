# Scraper Boilerplate

A crawler boilerplate implemented in scrapy framework that is using [scrapy-fake-useragent](https://github.com/alecxe/scrapy-fake-useragent) in order to pretend a randomized user agent per request and [scrapy-proxies](https://github.com/aivarsk/scrapy-proxies) to distribute requests over a pool of specified proxies declared in proxy_list.txt

Furthermore, a local MongoDB is used to store extracted items.
