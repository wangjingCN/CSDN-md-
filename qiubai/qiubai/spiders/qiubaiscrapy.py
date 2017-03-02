# -*- coding: utf-8 -*-
import scrapy
from qiubai.items import QiubaiItem
import re

class QiubaiscrapySpider(scrapy.Spider):
    name = "qiubaiscrapy"
    allowed_domains = ["qiubaichengren.com"]
    # start_urls = ['http://www.qiubaichengren.com/%s.html' % i for i in range(1, 21)]
    start_urls = ['http://www.qiubaichengren.com/1.html']

    def parse(self, response):
        reg = r'<img alt="(.*)" src="(.*)" style=".*?" />'
        html = response.body
        results = re.findall(reg, html, re.M)
        for result in results:
            qb = QiubaiItem()
            # qb['alt'] = result[0].encode('utf-8').decode("gbk")  # 怎么解决中文问题啊
            qb['image_urls'] = result[1]
            # 从url_str = 'http://wx4.sinaimg.cn/mw600/661eb95cgy1fd49qw0f97j20s00utn68.gif'中找出 661eb95cgy1fd49qw0f97j20s00utn68.gif
            name_reg = r'[^\/]+$'
            # qb['images'] = re.findall(name_reg, result[1])[0]
            qb['images'] =result[1]
            # print 'result<<<<<<<',re.findall(name_reg, result[1])[0]
            yield qb