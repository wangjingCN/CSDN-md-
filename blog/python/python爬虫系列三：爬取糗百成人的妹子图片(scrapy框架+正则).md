#python爬虫系列三：爬取糗百成人的妹子图片(scrapy框架+正则)
#windows下scrapy的安装
具体的安装使用，详见scrapy官网：[http://scrapy-chs.readthedocs.io/zh_CN/0.24/intro/tutorial.html](http://scrapy-chs.readthedocs.io/zh_CN/0.24/intro/tutorial.html)
1.pip install scrapy
2.安装py32，我的CSDN资源路劲[http://download.csdn.net/detail/u010445540/9769285](http://download.csdn.net/detail/u010445540/9769285)
3，pip install pillow
#安装scrapy之后，执行命令 scrapy startproject qiubai，自动生成scrapy基础框架
	 main.py #这个文件是自己编写的，用来代替命令行启动
	 qiubaiscrapy.csv #这个是启动之后生成的数据
	 scrapy.cfg
	─qiubai
	 │  items.py
	 │  items.pyc
	 │  middlewares.py
	 │  pipelines.py #管道文件
	 │  pipelines.pyc
	 │  settings.py
	 │  settings.pyc
	 │  __init__.py
	 │  __init__.pyc
	 │
	 └─spiders
	         qiubaiscrapy.py #定义的spider
	         qiubaiscrapy.pyc
	         __init__.py
	         __init__.pyc

#爬取糗百成人的妹子图片[http://blog.csdn.net/u010445540/article/details/59486230](http://blog.csdn.net/u010445540/article/details/59486230)要定义的文件

##items.py（带爬资源的模型文件）
	from  scrapy import Item, Field
	
	
	class QiubaiItem(Item):
	    image_urls = Field()
	    images = Field()

##qiubaiscrapy.py（定义爬虫程序）
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
	

##启动scrapy（main.py）

	#!/usr/bin/env python
	# -*- coding: utf-8 -*-
	from scrapy import cmdline
	cmdline.execute('scrapy crawl qiubaiscrapy -o qiubaiscrapy.csv -t csv '.split())

**ps：这个scrapy框架，实现的很简单，只是像我爬虫系列中的前2章一样，并没有太多复杂的逻辑，但是他的优点是可以不再spider，直接推到管道中处理，实现更加复杂的逻辑**