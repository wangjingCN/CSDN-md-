#python操作Excel时,对datetime格式的处理
	背景：朋友不会Excel也不会程序语言，对Excel又有些很复杂的操作要求，问我会不会。
	我当然不会EXCEL，也懒得去学vba的语法，于是我想到了用python给他来做一个小工具来解决他的问题。
我的博客中之前已经介绍过python GUI开发环境的准备工作。
<http://blog.csdn.net/u010445540/article/details/52585333> 
>这里来讨论下python处理datetime格式时，遇到的大坑，以及解决办法。

##模拟需求：
我们有两张表格，分别叫：混合数据.xlsx，固定部分，xlsx

						混合数据.xlsx
	序号 | 日期 | 金额 |　经手人｜　过手人
	----|------|------|------|------
	１ | 2016/9/18 | 9.88  | 张三3 | A
	２ | 2016/9/19  | 10.88| 张三 | B
	３ | 2016/9/20  | 11.88| 2016/9/18 | A


						基础数据.xlsx
	序号 
	----
	１ 
	３

现在我们需要根据基础数据中的序列号，对混合数据进行筛选，得到如下表格：

							new_混合数据.xlsx
	序号 | 日期 | 金额 |　经手人｜　过手人 | 是否包含
	----|------|------|------|------|------
	１ | 2016/9/18 | 9.88  | 张三3 | A | 是
	２ | 2016/9/19  | 10.88| 张三  | B | 否
	３ | 2016/9/20  | 11.88| 张三  | A | 是
新生成的表格对重合的序号进行了"标红，加粗",并且新生成了一列"是否包含"

##代码部分

	#!/usr/bin/env python
	# -*- coding: utf-8 -*-
	from xlrd import open_workbook, xldate
	from xlutils.copy import copy
	import xlwt
	
	def edit_excel(filename, base_id=[]):
	    font0 = xlwt.Font()
	    font0.name = 'Times New Roman'
	    font0.colour_index = 2  # 红色
	    font0.bold = True
	
	    style0 = xlwt.XFStyle()
	    style0.font = font0
	
	    style1 = xlwt.XFStyle()
	    style1.num_format_str = 'YYYY/MM/DD'  # 对日期格式的处理
		# style1.num_format_str = u'MM月DD日'  # 对日期格式的处理	

	    rb = open_workbook(filename)
	    # rb_cols_len = rb.sheet_by_index(0).ncols  # 原表的列数
	    wb = copy(rb)
	    ws = wb.get_sheet(0)
	    table = rb.sheets()[0]
	    for row_number in range(table.nrows):
	        if row_number == 0:
	            ws.write(0, 5, u"是否包含", style0)  # 新增一列
	
	        else:
	            if table.row_values(row_number)[0] in base_id:
	                ws.write(row_number, 0, table.row_values(row_number)[0], style0)  # 这个地方需要改一个颜色
	                ws.write(row_number, 5,u'是', style0)  # 给新增的列添加内容
	            else:
	                ws.write(row_number, 5,u'否')  # 给新增的列添加内容
	            ws.write(row_number, 1, xldate.xldate_as_datetime(table.row_values(row_number)[1], 0), style1)  # 这个地方需要写成日期格式
	
	
	    # wb.save(filename)#覆盖原文件
	    wb.save('new_' + filename)  # 可以把文件保存为另外的名字，原文件不会改变
	    print 'ok'
	
	
	def get_excel_base_ids(base_filename):
	    data = open_workbook(base_filename)  # 打开xls文件
	    base_id = []
	    table = data.sheets()[0]  # 打开第一张表
	    for i in range(table.nrows):  # 按行循环
	        if i:  # 跳过第一行
	            base_id.append(table.row_values(i)[0])
	    return base_id
	
	
	# print get_base_ids(u'固定部分.xlsx')
	print edit_excel(u'混合数据.xlsx', get_excel_base_ids(u'固定部分.xlsx'))


##datetime的解决办法
混合数据的表中有个日期:2016/9/18

通过table.row_values(row_number)[1]读取时，显示的结果为：42631.0

查看row_values方法的源码：

    def row_values(self, rowx, start_colx=0, end_colx=None):
        if end_colx is None:
            return self._cell_values[rowx][start_colx:]
        return self._cell_values[rowx][start_colx:end_colx]

也就是说返回了self._cell_values，self._cell_values在源码中的定义为：self._cell_values = []，这就是问题的根源

**第一种解决办法:**

	xldate.xldate_as_datetime把日期转换回来
	xldate.xldate_as_datetime(table.row_values(row_number)[1], 0)
>

**第二种解决办法:**

>先用xldate.xldate_as_tuple(table.row_values(row_number)[1]，0)
>
>显示结果为：(2016, 9, 27, 0, 0, 0)
>
*xldate_as_tuple源码部分：*
>
	\# @param datemode 0: 1900-based, 1: 1904-based.
	xldate_as_tuple(xldate, datemode) 
>

>最后再用datetime.datetime(2016, 9, 27, 0, 0, 0)把日期转回来