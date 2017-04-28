# -*- coding: utf-8 -*-
import scrapy
from weixinpub.items import WeixinpubItem
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class ShihangSpider(CrawlSpider):
    name = 'shihang'
    allowed_domains = ['mp.weixin.qq.com']
    start_urls = ['https://mp.weixin.qq.com/s?__biz=MjM5NzcwNzgyMA==&mid=2650088974&idx=1&sn=5c65bd78d432fb1ea9edbb45478d17d1&chksm=bed46f4d89a3e65b940d7ec0d19da2e6da369ed63521df3d7e0cb2151c3f4c0e929c4847de05&scene=0#rd/']

    rules = (
        Rule(LinkExtractor(allow=r''), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        print(response)
        item = WeixinpubItem()
        item['title'] = "test"
        #item['title'] = response.css('h2#activity-name::text').extract()
        item['url'] = response.status

        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return item
