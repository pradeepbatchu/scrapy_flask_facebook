import jsons
import scrapy
from scrapy import Request
from scrapy.crawler import CrawlerProcess
from scrapyproject.items import FacebookItem


class facebookSpider(scrapy.Spider):
    name = 'facebook'

    def parse(self, response):
        print(response.url)
        items = FacebookItem()
        business_phone = response.xpath('.//div[1][@class="_4-u2 _3xaf _3-95 _4-u8"]/div[@class="_5aj7 _3-8j"]/div[@class="_4bl9"]/div[@class="_50f4"]/text()').extract_first()
        mission = response.xpath('.//div[@class="_5aj7 _3-8j"][1]/div[@class="_4bl9"]/div[@class="_3-8w"]/text()').extract_first()
        company_overview = response.xpath('.//div[@class="_5aj7 _3-8j"][2]/div[@class="_4bl9"]/div[@class="_3-8w"]/text()').extract_first()
        company_address = response.xpath('.//div[@class="_5aj7 _3-8j _20ud"]/div[@class="_4bl9"]/div[1]/span[@class="_2iem"]/text()').extract_first()
        company_address1 = response.xpath('.//div[@class="_5aj7 _3-8j _20ud"]/div[@class="_4bl9"]/div[2]/span[@class="_2iem"]/text()').extract_first()

        closed_open = response.xpath('.//span[@class="_14-5"]/text()').extract_first()
        office_hours = response.xpath('..//div[@class="clearfix _ikh _5jau _p"]/div[@class="_4bl7"]/text()').extract_first()

        founding_date = response.xpath('.//div[1]/div[2][@class="_5aj7 _3-8j"]//div[@class="_50f4"]/text()').extract_first()
        price_range = response.xpath('..//div[@class="clearfix _ikh _3-95"]/div[@class="_4bl9 _5k_"]/span/text()').extract_first()
        weburl = response.xpath('.//div[@class="_2nx_ _2rgt _1j-g _2rgt"]/div[@class="_9_7 _2rgt _1j-f _2rgt"]/div[@class="_59k _2rgt _1j-f _2rgt _7-v _3zi4 _2rgt _1j-f _2rgt"]/text()').extract_first()
        email = response.xpath('.//a/div[@class="_50f4"]/text()').extract_first()
        awards = response.xpath('.//div[6][@class="_5aj7 _3-8j"]/div[@class="_4bl9"]/div[@class="_3-8w"]/text()').extract()
        milestones = response.xpath('.//li[1][@class="_2lch"]/span/text()').extract_first()
        cell = response.xpath('.//div[4][@class="_4-u2 _3xaf _3-95 _4-u8"]/div[@class="_5aj7 _3-8j"]/div[@class="_4bl9"]/div[@class="_50f4"]/text()').extract_first()
        products = response.xpath('.//div[@class="_5aj7 _3-8j"][5]/div[@class="_4bl9"]/div[@class="_3-8w"]/text()').extract_first()
        categories = response.xpath('.//div[@class="_4bl9 _5m_o"]/a[1]/text()').extract()
        search_pages2 = response.xpath('.//div[@class="_4bl9 _5m_o"]/a[2]/text()').extract_first()
        image = response.css('img ::attr(data-src)').extract_first()

        items['url'] = response.request.url
        #items['business_phone'] = business_phone
        items['mission'] = mission
        items['company_address'] = company_address
        items['company_address1'] = company_address1
        items['closed_open'] = closed_open
        items['office_hours'] = office_hours
        items['company_overview'] = company_overview
        items['founding_date'] = founding_date
        #items['price_range'] = price_range
        items['weburl'] = weburl
        #items['weburl1'] = weburl1
        items['email'] = email
        items['cell'] = cell
        items['awards'] = awards
        items['milestones'] = milestones
        items['products'] = products
        items['categories'] = categories
        #items['search_pages2'] = search_pages2
        items['image'] = image
        final = jsons.dumps(items)
        return items


