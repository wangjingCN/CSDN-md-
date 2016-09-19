#!/usr/bin/env python
# -*- coding: utf-8 -*-
from xlrd import open_workbook
from xlutils.copy import copy
import xlwt


def edit_file(filename, base_id=[]):
    font0 = xlwt.Font()
    font0.name = 'Times New Roman'
    font0.colour_index = 2 #红色
    font0.bold = True

    style0 = xlwt.XFStyle()
    style0.font = font0

    rb = open_workbook(filename)
    wb = copy(rb)
    ws = wb.get_sheet(0)
    # table = rb.get_sheet()[0] #这个方法好像过时了
    table = rb.sheets()[0]
    for row_number in range(table.nrows):
        if row_number:
            if table.row_values(row_number)[0] in base_id:
                ws.write(row_number, 0, table.row_values(row_number)[0],style0)  # 这个地方需要改一个颜色
                # ws.write(row_number, 0, 'change',style0)  # 这个地方需要改一个颜色
    wb.save(filename)
    print 'ok'


def get_base_ids(base_filename):
    data = open_workbook(base_filename)  # 打开xls文件
    base_id = []
    table = data.sheets()[0]  # 打开第一张表
    for i in range(table.nrows):  # 按行循环
        if i:  # 跳过第一行
            base_id.append(table.row_values(i)[0])
    return base_id

# print get_base_ids(u'固定部分.xlsx')
print edit_file(u'混合数据.xlsx',get_base_ids(u'固定部分.xlsx'))
