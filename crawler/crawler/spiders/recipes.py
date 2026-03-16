import scrapy


class RecipesSpider(scrapy.Spider):
    name = "recipes"
    allowed_domains = ["hungrylankan.com"]
    start_urls = ["https://hungrylankan.com"]

    def parse(self, response):
        pass
