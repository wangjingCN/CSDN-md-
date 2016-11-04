#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urlparse
import re
from urllib2 import Request, urlopen, URLError


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


def get_links(html):
    links_regex = re.compile('<a[^>]+href=["\'](. *?)["\']', re.IGNORECASE)
    return links_regex.findall(html)


def link_crawler(seed_url, url_regx):
    link_list = [seed_url]
    while link_list:
        url = link_list.pop()
        html = get_url_content(url)
        print html
        for link in get_links(html):
            if re.match(url_regx, link):
                link=urlparse.urljoin(seed_url,link)
                print link
                link_list.append(link)


url = "http://example.webscraping.com"
url_regex = "/(index/view)"
link_crawler(url, url_regex)
