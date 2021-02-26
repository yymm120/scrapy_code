# Readme

| 知识点       | 已掌握                                                       |
| ------------ | ------------------------------------------------------------ |
| scrapy       | Pipeline、middleware等组件、scrapy_redis、splash、请求构造、部署等 |
| redis        | 安装、常用命令、redis模块使用、scrapy_redis模块使用          |
| 分布式爬虫   | 概念、实现、部署，使用Gerapy框架管理。                       |
| 爬取豆瓣影评 | 使用scrapy爬取影评。                                         |
| 爬取分类电影 | 共17类别，8337部电影信息。使用远程mongo数据库存储。          |



## scrapy_douban

### [mongo_project1](./scrapy_douban/scrapy_douban/spiders/mongo_project1.py) 项目

进入项目路径

`cd scrapy_douban` 

运行爬虫

`scrapy runspider  mongo_project1.py -o ../../data/%(name)s.json` 

### mongodb存储

如果使用mongodb存储，则改写`MongoMoviePipeline` ，并在spider中配置custom_settings

```python
# mongo_project1Spider.py
custom_settings = {
        'ITEM_PIPELINES': {'scrapy_douban.pipelines.MongoMoviePipeline': 300,}
}
```

 改写mongodb服务

```python
# scrapy_douban.pipelines.py
class MongoMoviePipeline:
    def open_spider(self, spider):
        self.client = MongoClient("IP", 27017)
        self.db = self.client["admin"]
        self.db.authenticate("username", "passwd")
        self.col = self.db["tags_movies"]
```



### [film_reviews2](scrapy_douban/scrapy/douban/spider/film_reviews2.py) 项目

该项目爬取电影的影评，并保存到data目录中。

进入项目路径

`cd scrapy_douban` 

运行爬虫

`scrapy crawl film_reviews2 --nolog` 









