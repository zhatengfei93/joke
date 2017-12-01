# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JokeItem(scrapy.Item):
    # define the fields for your item here like:
    # 标题
    title = scrapy.Field()
    # 来源
    source = scrapy.Field()
    # 来源地址
    sourceUrl = scrapy.Field()
    # 内容
    content = scrapy.Field()
    # 查看全文
    DetailsText = scrapy.Field()
    # 点赞
    like = scrapy.Field()
