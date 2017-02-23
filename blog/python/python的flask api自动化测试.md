#python的flask api 自动化测试
	项目测试对于一个项目的重要性，大家应该都知道吧。写python的朋友，应该都写过自动化测试脚本。最近正好负责公司项目中的api测试，下面写了一个简单的例子，对API 测试进行梳理。

## 首先，编写restful api接口文件 testpost.py，包含了get，post，put方法

	#!/usr/bin/env python
	# -*- coding: utf-8 -*-
	from flask import request
	from flask_restful import Resource
	from flask_restful import reqparse
	
	
	test_praser = reqparse.RequestParser()
	test_praser.add_argument('ddos')


	class TestPost(Resource):
    def post(self, PostData):
        data = request.get_json()
        user = User('wangjing')
        if data['ddos']:
          return {'hello': 'uese', "PostData": PostData, 'ddos': 'data[\'ddos\']'}
        return {'hello': 'uese', "PostData": PostData}

    def get(self, PostData):
        data = request.args
        if data and data['ddos']:
            return "hello" + PostData + data['ddos'], 200
        return {'hello': 'uese', "PostData": PostData}

    def put(self, PostData):
        data = test_praser.parse_args()
        if data and data['ddos']:
            return "hello" + PostData + data['ddos'], 200
        return {'hello': 'uese', "PostData": PostData}

ps:对于request的取值，我这里定义了常用的三种方法：
> post方法：request.get_json(),在调用API时，传值是json方式

> get和put方法:request.args 或者reqparse.RequestParser(),调用API时，传的是字符串

## 其次，定义Blueprint（蓝图）文件 __init__.py
	#!/usr/bin/env python
	# -*- coding: utf-8 -*-
	from flask import Blueprint
	from flask_restful import Api
	from testpost import TestPost
	
	testPostb = Blueprint('testPostb', __name__)
	api = Api(testPostb)
	api.add_resource(TestPost, '/<string:PostData>/postMeth')

##然后,编写测试脚本testPostM.py
	#!/usr/bin/env python
	# -*- coding: utf-8 -*-
	import unittest
	import json
	from secautoApp.api.testPostMeth import api
	from flask import url_for
	from run import app
	from secautoApp.api.testPostMeth import TestPost
	
	headers = {'Accept': 'application/json',
	           'Content-Type': 'application/json'
	           }
	
	class APITestCase(unittest.TestCase):
	    def setUp(self):
	        # self.app = create_app(os.getenv("SECAUTOCFG") or 'default')
	        self.app = app
	        #     self.app_context = self.app.app_context()
	        #     self.app_context.push()
	        self.client = self.app.test_client()
	
	    #
	    # def tearDown(self):
	    #     self.app_context.pop()
	
	    def test_post(self):
	        # with app.test_request_context():
	
	        response = self.client.get(api.url_for(TestPost, PostData='adb', ddos='123'))
	        self.assertTrue(response.status_code == 200)
	
	        response = self.client.get(url_for('testPostb.testpost', PostData='adb', ddos='123'))
	        self.assertTrue(response.status_code == 200)	
			self.assertTrue(json.loads(response.data)['PostData'] =='adb')

	        response = self.client.post(url_for('testPostb.testpost', PostData='adb'), headers=headers,
	                                    data=json.dumps({"ddos": '123'}))
	        print json.loads(response.data)
	        self.assertTrue(response.status_code == 200)
	
	        response = self.client.put(url_for('testPostb.testpost', PostData='adb', ddos='123'))
	        self.assertTrue(json.loads(response.data) == 'helloadb123')
	
	        response = self.client.put(url_for('testPostb.testpost', PostData='adb'))
	        print json.loads(response.data)['PostData']
	        self.assertTrue(response.status_code == 200)

ps:调用的api url 主要用的是flask_restful 的api.url_for,或者是flask的url_for,下面我来说下这2种方法的具体使用

	flask_restful 的api.url_for说明
>api.url_for(TestPost,PostData='adb'),这里的TestPost指的是restful api接口文件中定义的class，因为我们在api蓝图中，已经通过api.add_resource(TestPost, '/<string:PostData>/postMeth')添加类的方式定义过

	flask的url_for的使用说明
>url_for('testPostb.testpost', PostData='adb', ddos='123'),'testPostb.testpost'这个字符串中
>
>testPostb指的是蓝图的名称，也就是testPostb = Blueprint('testPostb', __name__)中Blueprint('testPostb',__name__)中的testPostb。
>
>testpost指的是蓝图下endpoit的端点名称,flask_restful中，指的是api.add_resource(TestPost, '/<string:PostData>/postMeth')中 类名TestPost的小写

##启动测试脚本：

	C:\secauto3>python run.py test
	test_post (testPostM.APITestCase) ... ok
	
	----------------------------------------------------------------------
	Ran 1 test in 0.056s
	
	OK


小总结：url_for的传值和request中的取值是有对应关系的，最后就是flask_restful中端点的方式，一定要是api.add_resource中类名的小写

