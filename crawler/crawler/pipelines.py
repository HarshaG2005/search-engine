# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


import json
import os

class CrawlerPipeline:
    def open_spider(self, spider):
        self.recipes = []
        self.current_id = 1

    def process_item(self, item, spider):
        self.recipes.append({
            "id": self.current_id,
            "title": item.get("Titel", "").strip(),
            "ingredients": [i.strip() for i in item.get("ingridients", []) if i.strip()],
            "img_url": item.get("img_url", ""),
            "url": item.get("url", "")
        })
        self.current_id += 1
        return item

    def close_spider(self, spider):
        output_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'data', 'recipe.json')
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(self.recipes, f, indent=2, ensure_ascii=False)
        spider.logger.info(f"Saved {len(self.recipes)} recipes to recipe.json")