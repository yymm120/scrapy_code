import scrapy
from scrapy_douban.items import ScrapyDoubanItem

class FilmReviewsSpider(scrapy.Spider):
    name = 'film_reviews2'
    allowed_domains = ['douban.com']
    # start_urls = ["https://movie.douban.com/subject/" + "34841067" + "/comments?start={}".format(20 * i) for i in range(25)]
    start_urls = ["https://movie.douban.com/subject/" + "34841067" + "/comments?start=%(page)s" % {'page': str(20 * i)} for i in range(25)]
    custom_settings = {
        'ITEM_PIPELINES': {'scrapy_douban.pipelines.ScrapyDoubanPipeline1': 300}
    }

    # 使用cookies，需要重写start_requests方法。
    def start_requests(self):
        # url = self.start_urls[0]
        temp = 'bid=Cnjz9cBnj6w; douban-fav-remind=1; _vwo_uuid_v2=D11461EC51FE0345B5F25AFEFCD396C64|c9829af4519706a04637c0780002999d; gr_user_id=c461a612-3dd7-4b6f-baa4-326714aa744c; ll="108309"; __yadk_uid=fFfR7Csr20br8zxrKshH7b1zzeUiWgr6; viewed="25835263_6432399_6067994_35028385_4854123"; __gads=ID=68592c1189196044-22496ad964c50056:T=1609501496:RT=1609501496:R:S=ALNI_MYiNUFueC4D30lol-QqroQ2p2PeYw; ct=y; _ga=GA1.2.1699190019.1595046604; __utmz=30149280.1613749534.29.21.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmc=30149280; __utmz=223695111.1613749534.19.13.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmc=223695111; dbcl2="229176730:URmBAvJmuJk"; ck=q2MB; douban-profile-remind=1; push_noty_num=0; push_doumail_num=0; __utmv=30149280.22917; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1613811859%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D; _pk_ses.100001.4cf6=*; __utma=30149280.1699190019.1595046604.1613749534.1613811860.30; __utma=223695111.475014747.1595559137.1613749534.1613811860.20; __utmb=223695111.0.10.1613811860; ap_v=0,6.0; __utmt_douban=1; __utmb=30149280.31.10.1613811860; _pk_id.100001.4cf6=43d467f010407866.1595559138.20.1613815345.1613750788.'
        cookies = {cookie.split("=")[0]: cookie.split("=")[-1] for cookie in temp.split("; ")}
        for url in self.start_urls:
            yield scrapy.Request(
                url=url,
                callback=self.parse,
                cookies=cookies,
            )

    def parse(self, response):
        items = ScrapyDoubanItem()
        items["movie_reviews"] = []
        data = response.xpath('//*[@id="comments"]/div/div[2]/p/span/text()').extract()
        items["movie_reviews"].extend([i for i in data])
        yield items