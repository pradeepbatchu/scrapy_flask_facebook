import crochet
crochet.setup()  # initialize crochet before further imports

from flask import Flask, jsonify, request,abort
from scrapy import signals
from scrapy.crawler import CrawlerRunner
from scrapy.signalmanager import dispatcher
#from fbscrapy import QuotesSpider1
from scrapyproject.spiders.fbscpy import facebookSpider


app = Flask(__name__)
output_data = []
crawl_runner = CrawlerRunner()
# crawl_runner = CrawlerRunner(get_project_settings()) if you want to apply settings.py


@app.route("/scrape", methods=['POST'])
def scrape():
    if not request.json:
        abort(400)
    scrape.username = request.json['facebook_profile']
    # run crawler in twisted reactor synchronously
    scrape_with_crochet()

    return jsonify(output_data[0])



@crochet.wait_for(timeout=60.0)
def scrape_with_crochet():
    # signal fires when single item is processed
    # and calls _crawler_result to append that item
    dispatcher.connect(_crawler_result, signal=signals.item_scraped)
    username = scrape.username
    url = [f'https://www.facebook.com/pg/{username}/about/', ]
    eventual = crawl_runner.crawl(facebookSpider, start_urls = url)
    return eventual  # returns a twisted.internet.defer.Deferred


def _crawler_result(item, response, spider):
    """
    We're using dict() to decode the items.
    Ideally this should be done using a proper export pipeline.
    """

    output_data.clear()
    output_data.append(dict(item))


if __name__=='__main__':
    app.run(host='0.0.0.0', port=8083, debug=True, use_reloader=False)
