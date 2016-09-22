#!/usr/bin/env python
# -*- coding: utf-8 -*-
from urllib2 import Request, URLError, urlopen
import re
import urllib
import os


def get_url_content(url, retry_times=2, user_agent='wswp'):
    print 'Downloading: ', url
    try:
        headers = {'User-Agent': user_agent}
        req = Request(url, headers=headers)
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
    # for index in range(1, 755):  # 按照ID来爬整个网站
    for index in range(1, 4):  # 按照ID来爬整个网站
        src = "http://www.qiubaichengren.com/%s.html" % (index)
        url_content = get_url_content(src)
        if url_content:
            son_save_path = mkdir(save_path + str(index) + "\\")
            pic_list = get_pic_url(url_content)
            for i in range(len(pic_list)):
                pic_url = pic_list[i][0]
                save_pic_urllib(son_save_path, pic_url)
            print '第' + str(index) + '页，爬取完毕。撸叼屎,拿去撸吧！'
