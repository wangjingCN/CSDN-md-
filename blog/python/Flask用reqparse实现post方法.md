	Flask用reqparse实现post方法时，parser.parse_args()的值为None的解决办法

##Flask—restful 的restful API实现
	from flask import Flask
	from flask_restful import Api, Resource, reqparse
	
	parser = reqparse.RequestParser(trim=True)
	parser.add_argument('name', location=['json', 'args'])
	
	parser2 = reqparse.RequestParser()
	parser2.add_argument('age', location=['json', 'args'])
	
	app = Flask(__name__)
	api = Api(app)
	
	
	class HelloWorld(Resource):
	    def get(self):
	        args = parser.parse_args()
	        args2 = parser2.parse_args()
	        print  args['name']
	        return {'name': args['name'], 'age': args2['age']}
	
	    def post(self):
	        args = parser.parse_args()
	        args2 = parser2.parse_args()
	        print  args['name']
	        return {'name': args['name'], 'age': args2['age']}
	
	
	api.add_resource(HelloWorld, '/p')
	
	if __name__ == '__main__':
	    app.run(debug=True)

**get 方法的调用：**
>
>http://127.0.0.1:5000/p?name=helo&&age=16



**post 方法的调用**：
>
>http://127.0.0.1:5000/p
>
>参数：
{
"name":"wangjing",
"age":"18"
}

>header:
Content-Type: application/json

##记录Flask—restful API 的一个坑：
**第一次用parser.add_argument('name')来定义request参数，post方法调用时：args = parser.parse_args()，获得的值为None**

>WFlask_restful源码中location的定义：

	_friendly_location = {
    u'json': u'the JSON body',
    u'form': u'the post body',
    u'args': u'the query string',
    u'values': u'the post body or the query string',
    u'headers': u'the HTTP headers',
    u'cookies': u'the request\'s cookies',
    u'files': u'an uploaded file',
	}

所以为了让定义的parser参数能同时支持get和post方法，location必须定义为：

location=['json', 'args']，不然的话，args = parser.parse_args()获取值的时候，args会为None