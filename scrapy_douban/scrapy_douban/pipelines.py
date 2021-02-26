import json
from pymongo import MongoClient
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class ScrapyDoubanPipeline1:
    def open_spider(self, spider):
        self.file = open('../../data/%(spider)s.json' % {'spider': spider.name}, 'w', encoding="utf-8")

    def process_item(self, item, spider):
        temp = dict(item)
        json_data = json.dumps(temp, ensure_ascii=False) + ',\n'
        self.file.write(json_data)
        return item

    def close_spider(self, spider):
        self.file.close()

# class ScrapyDoubanMongoPipeline:
#     def open_spider(self, spider):
#         self.client = MongoClient("106.13.90.85", 27017)
#         self.db = self.client["admin"]
#         self.col = self.db["movie_reviews"]
#
#     def process_item(self, item, spider):
#         temp = dict(item)
#         self.col.insert(temp)
#         return item
#
#     def close_spider(self, spider):
#         self.client.close()


class MongoMoviePipeline:
    def open_spider(self, spider):
        # self.file = open("./tag_douban.json", "w", encoding="utf-8")
        self.client = MongoClient("IP", 27017)
        self.db = self.client["admin"]
        self.db.authenticate("username", "passwd")
        self.col = self.db["tags_movies"]

    def process_item(self, item, spider):
        temp = dict(item)
        # json_data = json.dumps(temp, ensure_ascii=False) + ',\n'
        # self.file.write(json_data)
        self.col.insert(temp)
        return item

    def close_spider(self, spider):
        # self.file.close()
        self.client.close()

class RedisPipeline:
    def open_spider(self, spider):
        # self.file = open("./tag_douban.json", "w", encoding="utf-8")
        self.client = MongoClient("IP", 27017)
        self.db = self.client["admin"]
        self.db.authenticate("username", "passwd")
        self.col = self.db["tags_movies"]

    def process_item(self, item, spider):
        temp = dict(item)
        # json_data = json.dumps(temp, ensure_ascii=False) + ',\n'
        # self.file.write(json_data)
        self.col.insert(temp)
        return item

    def close_spider(self, spider):
        # self.file.close()
        self.client.close()