import scrapy
from crawler.items import RecipeScraperItem

class RecipesSpider(scrapy.Spider):
    name = "recipes"
    allowed_domains = ["hungrylankan.com"]
    start_urls = ["https://www.hungrylankan.com/recipe-cuisine/srilankan/"]

    def parse(self, response):
        # iterate over each recipe card on the listing page
        for recipe in response.css('div.dr-archive-single'):
            recipe_url = recipe.css("a[itemprop='url']::attr(href)").get()
            if recipe_url:
                yield scrapy.Request(url=recipe_url, callback=self.parse_recipe)
            else:
                self.logger.warning(f"Could not find url on page: {response.url}")

        # pagination — let the site tell you the next page
        next_page = response.css('a.next.page-numbers::attr(href)').get()
        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse)

    def parse_recipe(self, response):
        recipe=RecipeScraperItem()
        recipe["Title"]=response.css('h2.dr-title::text').get()
        recipe["ingredients"]=response.css('li.recipe-ingredient label::text').getall()
        recipe["img_url"]=response.css('div.dr-image img::attr(src)').get()
        recipe["url"]=response.url
        yield recipe