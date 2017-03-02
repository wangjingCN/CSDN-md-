#python爬虫系列二：爬取糗百成人的妹子图片(requests+正则)

在我的上篇文章：python爬虫系列一：爬取糗百成人的妹子图片中，体现的主要还是代码，这一次我用了更加流行的requests 和正则来改写代码，并且简单的说说思路

##爬取图片到底要干什么

	1，定义要爬取的页面。
糗百官网：http://www.qiubaichengren.com，里面是不是有很多的妹子图片，我们就是要把这些妹子图片爬取下来。接着我们点击‘下一页’按钮，发现网址变成了http://www.qiubaichengren.com/2.html,也就是要爬完所有的妹子图片，只需要找到末页标签就可以了http://www.qiubaichengren.com/850.html，

>所以我们要定义一个url_list=['http://www.qiubaichengren.com/%s.html' % i for i in range(1, 851)]确保访问了我们需要爬取的所有页面。

	2，找到要爬出图片的url
在http://www.qiubaichengren.com页面查看源码,发现图片都包含在 `<img alt="你点嘛，你点什么都很可口，我爱吃" src="http://wx2.sinaimg.cn/mw600/661eb95cly1fd3nbpczarj20jz0zk47g.jpg" style="width: 350px; height: 623px;" />`这样的标签里面，为了找到页面中所有的img标签，并提取alt 和src的内容，定义如下正则：
>`reg = r'<img alt="(.*)" src="(.*)" style=".*?" />'`
	
	3.找到图片名称
找到了图片的src="http://wx2.sinaimg.cn/mw600/661eb95cly1fd3nbpczarj20jz0zk47g.jpg",从src中提取661eb95cly1fd3nbpczarj20jz0zk47g.jpg文件名,定义正则如下
>url_reg = r'[^\/]+$'

4.下载图片
	ir = requests.get(image_url)
	if ir.status_code == 200:
	    open('logo.jpg', 'wb').write(ir.content)

##根据上文的思路，现在开始coding
	# !/usr/bin/env python
	# -*- coding: utf-8 -*-
	import requests
	from requests.exceptions import RequestException
	import re
	import os
	
	
	def get_url_content(url, retry_times=2):
	    print 'Downloading: ', url
	    try:
	        send_headers = {
	            'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0',
	            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	            'Connection': 'keep-alive'
	        }
	        html_content = requests.get(url, headers=send_headers).content.decode('gbk').encode('utf-8')  # 解决中文乱码问题
	    except RequestException, e:
	        html_content = None
	        print "retry times:", retry_times
	        if retry_times > 0:
	            if hasattr(e, 'code') and 500 <= e.code < 600:
	                get_url_content(url, retry_times - 1)
	    return html_content
	
	
	def download_pic(save_path, pic_url):
	    pic_name_reg = r'[^\/]+$'  # 根据src找到pic_name
	    pic_name = re.findall(pic_name_reg, pic_url)[0]
	    if not os.path.exists(save_path + pic_name):
	        r = requests.get(pic_url)
	        if r.status_code == 200:
	            open(save_path + pic_name, 'wb').write(r.content)
	
	
	def mkdir(mkdir_path):
	    path = mkdir_path.strip()
	    if not os.path.exists(path):
	        os.makedirs(path)
	    return path
	
	
	if __name__ == "__main__":
	    save_path = mkdir("/meizi/")
	    url_list = ['http://www.qiubaichengren.com/%s.html' % i for i in range(1, 806)]
	    for index, url in enumerate(url_list):
	        htm_content = get_url_content(url)
	        if htm_content:
	            pic_save_path = mkdir(save_path + str(index + 1) + "/")
	            src_reg = r'<img alt="(.*)" src="(.*)" style=".*?" />'  # 找到页面的所有src
	            for pic_alt, pic_src in re.findall(src_reg, htm_content, re.M):
	                print '图片介绍:', pic_alt, pic_src
	                download_pic(pic_save_path, pic_src)
	            print '第' + str(index + 1) + '页，爬取完毕。撸叼屎,拿去撸吧！'
