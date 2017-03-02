#python系列一：爬取糗百成人的所有妹子图片（urllib2）
>撸叼屎是我朋友，单身已久，每天让我给介绍妹子，于是我写了一个python爬虫来暂时满足他。
##给撸叼屎的程序
	#!/usr/bin/env python
	# -*- coding: utf-8 -*-
	from urllib2 import Request, URLError, urlopen
	import re
	import urllib
	import os
	
	
	def get_url_content(url, retry_times=2):
	    print 'Downloading: ', url
	    try:
	        send_headers = {
	            'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0',
	            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	            'Connection': 'keep-alive'
	        }
	        req = Request(url, headers=send_headers)
	        html_content = urlopen(req).read().decode('gbk', 'ignore').encode('utf-8')  # 此处对中文字符进行了转码
	    except URLError, e:
	        print e.reason
	        html_content = None
	        print "retry times:", retry_times
	        if retry_times > 0:
	            if hasattr(e, 'code') and 500 <= e.code < 600:
	                get_url_content(url, retry_times - 1)
	    return html_content
	
	
	def get_pic_url(html_content):
	    pic_reg = 'src="(http://.*?(png|jpg|gif))"'
	    patten = re.compile(pic_reg, re.IGNORECASE)
	    return patten.findall(html_content)
	
	
	def save_pic_urllib(save_path, pic_url):
	    save_pic_name = save_path + pic_url.split('/')[len(pic_url.split('/')) - 1]
	    if not os.path.exists(save_pic_name):
	        print save_pic_name
	        urllib.urlretrieve(pic_url, save_pic_name)
	
	
	def mkdir(mkdir_path):
	    path = mkdir_path.strip()
	    if not os.path.exists(path):
	        os.makedirs(path)
	    return path
	
	
	# print get_url_content("http://httpstat.us/500")
	if __name__ == "__main__":
	    save_path = mkdir("C:\\meizi\\")
	    for index in range(1, 755):  # 按照ID来爬整个网站
	        src = "http://www.qiubaichengren.com/%s.html" % (index)
	        url_content = get_url_content(src)
	        if url_content:
	            son_save_path = mkdir(save_path + str(index) + "\\")
	            pic_list = get_pic_url(url_content)
	            for i in range(len(pic_list)):
	                pic_url = pic_list[i][0]
	                save_pic_urllib(son_save_path, pic_url)
	            print '第' + str(index) + '页，爬取完毕。撸叼屎,拿去撸吧！'

整个程序可以直接运行，并且亲自测试，没有下载的图片，出现破损，不能看的问题。图片很劲爆

##说说写这个小爬虫遇到的小问题，urllib.urlretrieve()保存图片，有无法打开的问题

解决办法：设置了详细的headers。

	send_headers = {
	            'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0',
	            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	            'Connection': 'keep-alive'
	        }

##这个爬虫实现了哪些功能
  1.可以按照页面来创建文件夹

  2当出现了http_code ,500问题时，自动重新下载2次

  3，下载过的图片，自动跳过
  
  4，解决了图片下载不能打开的问题


##写在最后：身边有很多单身的优秀程序员，等着单身的你。缘分E-mail：289363142@qq.com