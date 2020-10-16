from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


from scrapyproject.spiders.fbscpy import facebookSpider

process = CrawlerProcess(get_project_settings())
process.crawl(facebookSpider)
#process.crawl(ZomatoSpider)
process.start()
