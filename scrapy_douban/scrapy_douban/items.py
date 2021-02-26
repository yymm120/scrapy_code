# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyDoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # 电影名称
    movie_name = scrapy.Field()
    # 电影详情页url
    movie_url = scrapy.Field()
    # 全部影评
    movie_reviews = scrapy.Field()
    # 电影导演
    movie_director = scrapy.Field()
    # 演员
    movie_actors = scrapy.Field()
    # 电影类型
    movie_style = scrapy.Field()
    # 豆瓣评分
    movie_score = scrapy.Field()
    # 上映时间
    movie_time = scrapy.Field()
    # 封面图片
    movie_pic = scrapy.Field()


class RedisDoubanItem(scrapy.Item):
    """
    目标：豆瓣电影 https://movie.douban.com/explore
    标签：热门 最新 经典 可播放 豆瓣高分 冷门佳片 华语 欧美 韩国 日本 动作 喜剧 爱情 科幻 悬疑 恐怖 动画
    标签对应的url：
    电影名：
    封面：
    豆瓣评分：
    电影详情url
    电影id
    """
    tag = scrapy.Field()
    tag_url = scrapy.Field()
    info = scrapy.Field()
    movie_name = scrapy.Field()
    movie_pic = scrapy.Field()
    movie_score = scrapy.Field()
    movie_id = scrapy.Field()
    movie_url = scrapy.Field()


