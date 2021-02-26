import scrapy
import json
from jsonpath import jsonpath
from scrapy_douban.items import RedisDoubanItem


# redis
class mongo_project1Spider(scrapy.Spider):
    name = 'mongo_project1'
    allowed_domains = ['douban.com']
    start_urls = ['https://movie.douban.com/j/search_tags?type=movie']

    custom_settings = {
        'ITEM_PIPELINES': {'scrapy_douban.pipelines.MongoMoviePipeline': False,}
    }
    # def start_requests(self):
    #     url = 'https://movie.douban.com/j/search_tags?type=movie'
    #     tags =
    #     movie_url = ['https://movie.douban.com/j/search_subjects?type=movie&tag=' + tag + '&page_limit=1000&page_start=0' for tag in tags]

    def parse(self, response):
        """
        tag: https://movie.douban.com/j/search_tag?
        电影：https://movie.douban.com/j/search_subjects?type=movie&tag=热门&page_limit=1000&page_start=0
             每1000部电影一页
        """
        item = RedisDoubanItem()
        item["tag"] = {}
        tags = json.loads(response.body)

        for tag in tags["tags"]:
            print(tags["tags"])
            yield scrapy.Request(
                url='https://movie.douban.com/j/search_subjects?type=movie&tag=' + tag + '&page_limit=1000&page_start=0',
                callback=self.movie_parse,
                meta={"tag": tag, "item": item}
            )

    def movie_parse(self, response):
        """
        大部分标签内的电影只有500部。
        这里以1000个电影一页进行访问。"&page_limit=1000"
        如果页面中的电影个数刚好等于1000，则尝试访问下一页。
        """
        # 初始化
        tag = response.meta["tag"]
        item = response.meta["item"]
        n = 0
        try:
             n = response.meta["movie_num"]
        except:
            pass
        text = json.loads(response.body)["subjects"]
        movie_num = len(text)  # 标签的电影数量，如果超过了1000，则加上第二页的movie_num

        for i in range(movie_num):
            item["tag"]["total_movie_num"] = movie_num + n  # 如果翻过页，该标签的电影数要加1000
            item["tag"]["tag_url"] = "https://movie.douban.com/j/search_subjects?type=movie&tag=" + tag
            item["movie_name"] = jsonpath(text, "$..title")[i]
            item["movie_score"] = jsonpath(text, "$..rate")[i]
            item["movie_id"] = jsonpath(text, "$..id")[i]
            item["movie_pic"] = jsonpath(text, "$..cover")[i]
            item["movie_url"] = jsonpath(text, "$..url")[i]
            yield item

        if movie_num // 1000:  # 0
            item["tag"]["total_movie_num"] = 1000
            # item.update(page_data(movie_num))
            yield scrapy.Request(
                url='https://movie.douban.com/j/search_subjects?type=movie&tag=' + tag + '&page_limit=2000&page_start=' + "1000",
                callback=self.movie_parse,
                meta={"item": item, "movie_num": 1000}
            )
