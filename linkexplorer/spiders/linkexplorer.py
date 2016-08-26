from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.http import Request
from bs4 import BeautifulSoup as bs
from linkexplorer.items import KompassAgentLink

class KompassExplorer(Spider):
    name = "linkexplorer"
    allowed_domains = ["kompass.com"]
    start_urls = ["http://de.kompass.com/"]

    # parse main page
    def parse(self, response):
        sel = Selector(response)
        county_xpath = '//div[@class="footerCol1-2"]/ul/li'
        county_markups = sel.xpath(county_xpath).extract()[:-1] # ignore all counties link
        for markup in county_markups:
            soup = bs(markup, 'lxml')
            comp_link = KompassAgentLink()
            c_link = 'http://de.kompass.com' + soup.find('a').get('href')
            c_name = soup.find('a').get_text()
            comp_link['county'] = c_name
            #self.logger.info('received link: ' + c_link + ' for county ' + c_name)
            request = Request(c_link, callback=self.parse_district)
            request.meta['comp_link'] = comp_link
            yield request

    # parse each filtered by county page to retrieve district links
    def parse_district(self, response):
        comp_link = response.meta['comp_link']
        sel = Selector(response)
        district_xpath = '//div[@class="filtres"]/div/div/div[@class="facetValues"]'
        district_markup = sel.xpath(district_xpath).extract()[0] # select district filter links
        for link in bs(district_markup, 'lxml').find_all('a'):
            self.logger.info("district markup is: " + str(link))
            d_link = response.url + link.get('href')
            self.logger.info('district url: ' + d_link)
            d_name = link.get_text().split(' ')[0]
            self.logger.info('found link: ' + d_link + ' for district ' + d_name)
            comp_link['district'] = d_name
            request = Request(d_link, callback=self.parse_sector)
            request.meta['comp_link'] = comp_link
            yield comp_link

    def parse_sector(self, response):
        pass
