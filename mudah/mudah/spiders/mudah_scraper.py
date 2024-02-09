import scrapy


class MudahScraperSpider(scrapy.Spider):
    name = "mudah_scraper"
    allowed_domains = ["mudah.my"]
    start_urls = ["https://www.mudah.my/selangor-cyberjaya/properties-for-rent?q=studio"]

    def parse(self, response):

        item = response.css 
        pass
