#python动态变量名和dict类型的list排序

数据模拟：

	menuData = [
    {"id": 0, "parent_id": -1, "sectionName": u"一键变更", "sectionURL": " ", "menu_level": 1},
    {"id": 1, "parent_id": 0, "sectionName": u"服务变更", "sectionURL": " ", "menu_level": 2},
    {"id": 2, "parent_id": 1, "sectionName": u"服务上线", "sectionURL": " www.baidu.com/fuwu/shangxian", "menu_level": 3},
    {"id": 3, "parent_id": 1, "sectionName": u"服务检查", "sectionURL": " www.baidu.com/wufu/jiancha", "menu_level": 3},
    {"id": 4, "parent_id": 1, "sectionName": u"服务执行", "sectionURL": " www.baidu.com/fuwu/zhixing", "menu_level": 3},
    {"id": 5, "parent_id": 0, "sectionName": u"域名变更", "sectionURL": " ", "menu_level": 2},
    {"id": 6, "parent_id": 5, "sectionName": u"域名上线", "sectionURL": "wwww.baidu.com/yuming/shagnxian ",
     "menu_level": 3},
    {"id": 7, "parent_id": 5, "sectionName": u"域名检查", "sectionURL": "wwww.baidu.com/yuming/jiancha ", "menu_level": 3},
    {"id": 8, "parent_id": 5, "sectionName": u"域名执行", "sectionURL": "wwww.baidu.com/yuming/zhixing ", "menu_level": 3},
    {"id": 9, "parent_id": -1, "sectionName": u"一键应急", "sectionURL": " ", "menu_level": 1},
    {"id": 91, "parent_id": 9, "sectionName": u"拒绝地址公鸡", "sectionURL": "www.baidu.cm ", "menu_level": 2}
]

##dict类型的list排序:
>上面的menuData，要按menu_level来排序

	level_num = sorted(menu_data, key=lambda k: (k['menu_level']), reverse=True)

>上面的menuData，要同时按menu_level和id来排序


	level_num = sorted(menuData, key=lambda k: (k['menu_level'],k['id']), reverse=True)

reverse参数代表降序排列

##动态变量名的使用:
>上面的menuData，要根据menu_level进行动态变量名的分组

	def get_menu_data_new(menu_data):
	names = locals()
    level_num = sorted(menu_data, key=lambda k: (k['menu_level']), reverse=True)[0]['menu_level']
    result = []
    for index in range(1, level_num + 1):
        names[str(index) + '_level'] = []
        for dataStr in menu_data:
            if dataStr['menu_level'] == index:
                names[str(index) + '_level'].append(dataStr)
        result.append(names[str(index) + '_level'])
    return result

动态变量名的使用要用到locals（）函数


