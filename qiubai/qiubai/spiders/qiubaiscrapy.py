# -*- coding: utf-8 -*-
import scrapy
from qiubai.items import QiubaiItem
import re
import os
import requests


class QiubaiscrapySpider(scrapy.Spider):
    name = "qiubaiscrapy"
    allowed_domains = ["qiubaichengren.com"]
    start_urls = ['http://www.qiubaichengren.com/%s.html' % i for i in range(1, 3)]

    def parse(self, response):
        if not os.path.exists('/meizi/'):
                os.makedirs('/meizi/')
        print 'xxxxx'
        reg = r'<img alt="(.*)" src="(.*)" style=".*?" />'
        html = response.body
        results = re.findall(reg, html, re.M)
        for result in results:
            qb = QiubaiItem()
            # qb['alt'] = result[0].decode("gbk").encode('utf-8')
            qb['image_urls'] = result[1]
            # 从url_str = 'http://wx4.sinaimg.cn/mw600/661eb95cgy1fd49qw0f97j20s00utn68.gif'中找出 661eb95cgy1fd49qw0f97j20s00utn68.gif
            name_reg = r'[^\/]+$'
            qb['images'] = re.findall(name_reg, result[1])[0]
            r = requests.get(qb['image_urls'])
            if r.status_code == 200:
                open(os.path.join('/meizi/', qb['images']), 'wb').write(r.content)
            yield qb
