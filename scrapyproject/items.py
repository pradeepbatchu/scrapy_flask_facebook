# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyprojectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class FacebookItem(scrapy.Item):
    # Items to get
    url = scrapy.Field()
    business_phone = scrapy.Field()
    mission = scrapy.Field()
    company_address = scrapy.Field()
    company_address1 = scrapy.Field()
    company_overview = scrapy.Field()
    founding_date = scrapy.Field()
    price_range = scrapy.Field()
    closed_open = scrapy.Field()
    office_hours = scrapy.Field()
    weburl = scrapy.Field()
    weburl1 = scrapy.Field()
    email = scrapy.Field()
    cell = scrapy.Field()
    awards = scrapy.Field()
    milestones = scrapy.Field()
    products = scrapy.Field()
    categories = scrapy.Field()
    search_pages2 = scrapy.Field()
    image = scrapy.Field()