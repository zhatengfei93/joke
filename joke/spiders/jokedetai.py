# -*- coding: utf-8 -*-
import scrapy
from joke.items import JokeItem

class JokedetaiSpider(scrapy.Spider):

    name = 'jokedetai'

    allowed_domains = ['http://xiaohua.zol.com.cn']

    # start_urls = ['http://xiaohua.zol.com.cn/detail31/30217.html']
    baseURL = "http://xiaohua.zol.com.cn/detail"
    detainumber = 0
    number = 1
    start_urls = [baseURL + str(detainumber) +"/"+str(number)+ ".html"]

    def parse(self, response):

        node_list = response.xpath("//div[@class='section article']")

        for node in node_list:

            item = JokeItem()

            title = node.xpath("./div[@class='article-header']/h1/text()").extract()
            if title:
                title = title[0]
                item['title'] = title

            source = node.xpath("./div[@class='article-header']/div[@class='article-source']/a/text()").extract()
            if source:
                source = source[0]
                item['source'] = source

            content = node.xpath("./div[@class='article-text']/text()").extract()
            if content:
                content = content[0]
                item['content'] = content

            like = node.xpath("./div[@class='article-commentbar articleCommentbar clearfix']/div[@class='good-btn-box vote-btn']/em[@class='good-btn']/span/text()").extract()
            if len(like) !=0:
                like = like[0]
                item['like'] = like

            yield item
        # if len(response.xpath("//div[7]/div[1]/div[1]/div[4]/span[1]/a").extract()) == 0:
        #     url = response.xpath("//div[7]/div[1]/div[1]/div[4]/span[1]/a/@href").extract()[0]
        #     yield scrapy.Request("http://xiaohua.zol.com.cn" + url, callback=self.parse)