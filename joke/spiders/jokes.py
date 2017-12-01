# -*- coding: utf-8 -*-
import scrapy
from joke.items import JokeItem

class JokesSpider(scrapy.Spider):
    name = 'jokes'
    allowed_domains = ['xiaohua.zol.com.cn']
    baseURL = "http://xiaohua.zol.com.cn/new/"
    offset = 0
    start_urls = [baseURL+str(offset)+".html"]

    def parse(self, response):
        node_list = response.xpath("//li[@class='article-summary']")
        for node in node_list:
            item = JokeItem()
            # item['content'] = node
            title = node.xpath("./span[@class='article-title']/a/text()").extract()
            if title:
                title = title[0]
                item['title'] = title

            source = node.xpath("./div[@class='article-source']/a/text()").extract()
            if source:
                source = source[0]
                item['source'] = source

            sourceUrl = node.xpath("./div[@class='article-source']/a/@href").extract()
            if sourceUrl:
                sourceUrl = sourceUrl[0]
                item['sourceUrl'] = sourceUrl

            content = node.xpath("./div[@class='summary-text']/text()").extract()
            if content:
                content = content[0]
                item['content'] = content

            DetailsText = node.xpath("./div[@class='article-commentbar articleCommentbar clearfix']/a/@href").extract()
            if DetailsText:
                DetailsText = DetailsText[0]
                item['DetailsText'] = DetailsText

            like = node.xpath("./div[@class='article-commentbar articleCommentbar clearfix']/div[@class='good-btn-box vote-btn']/em/span/text()").extract()
            if like:
                like = like[0]
                item['like'] = like

            yield item

        if self.offset < 2:
            self.offset += 1
            url = self.baseURL + str(self.offset) +".html"
            yield  scrapy.Request(url,callback = self.parse)