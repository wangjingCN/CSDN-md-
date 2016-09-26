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
            # "Host": "www.qiubaichengren.com",
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36',
            'Accept':'text/html, */*; q=0.01',
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


def save_pic_urllib(save_path, pic_url, retry_times=3):
    opener = urllib.FancyURLopener({})
    opener.verion = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36'
    print pic_url
    pic_name = pic_url.split('/')[len(pic_url.split('/')) - 1]
    if pic_name != '0068djjqjw1f467h575l3j308c05z75o.jpg':
        save_pic_name = save_path + pic_name
        try:
            opener.retrieve(pic_url, save_pic_name)
            # urllib.urlretrieve(pic_url, save_pic_name)
        except urllib.ContentTooShortError:
            print '下载出现了错误,现在对', save_pic_name, "重新下载"
            save_pic_urllib(save_path, pic_url, retry_times - 1)


def mkdir(mkdir_path):
    path = mkdir_path.strip()
    if not os.path.exists(path):
        os.makedirs(path)
    return path


# 0068djjqjw1f467h575l3j308c05z75o.jpg，这张照片需要过滤

# print get_url_content("http://httpstat.us/500")
if __name__ == "__main__":
    save_path = mkdir("C:\\meizi\\")
    # for index in range(1, 755):  # 按照ID来爬整个网站
    for index in range(52, 58):  # 按照ID来爬整个网站
        src = "http://www.qiubaichengren.com/%s.html" % (index)
        url_content = get_url_content(src)
        if url_content:
            son_save_path = mkdir(save_path + str(index) + "\\")
            pic_url_list = get_pic_url(url_content)
            for i in range(len(pic_url_list)):
                pic_url = pic_url_list[i][0]
                save_pic_urllib(son_save_path, pic_url)
            print '第' + str(index) + '页，爬取完毕。撸叼屎,拿去撸吧！'

    print '爬虫执行完毕'