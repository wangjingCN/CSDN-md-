# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from qiubai.settings import IMAGES_STORE
import os
import urllib
import requests


class QiubaiPipeline(object):
    def process_item(self, item, spider):
        if 'image_urls' in item:  # 如何‘图片地址’在项目中
            images = []  # 定义图片空集

            dir_path = '%s/%s' % (IMAGES_STORE, spider.name)

            if not os.path.exists(dir_path):
                os.makedirs(dir_path)
            for image_url in item['image_urls']:
                us = image_url.split('/')[3:]
                image_file_name = '_'.join(us)
                file_path = '%s/%s' % (dir_path, image_file_name)
                images.append(file_path)
                if os.path.exists(file_path):
                    continue

                with open(file_path, 'wb') as handle:
                    response = requests.get(image_url, stream=True)
                    for block in response.iter_content(1024):
                        if not block:
                            break

                        handle.write(block)

            item['images'] = images
        return item

        # def save_pic_urllib(save_path='/pic/', pic_url=None):
        #     save_pic_name = save_path + pic_url.split('/')[len(pic_url.split('/')) - 1]
        #     if not os.path.exists(save_pic_name):
        #         print save_pic_name
        #         urllib.urlretrieve(pic_url, save_pic_name)
