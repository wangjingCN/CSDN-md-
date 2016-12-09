Nginx 和 uWSGI 部署 Flask 应用

	不管是windows或者linux，首先我默认你已经了安装好了Nginx和uwsgi，这里要谈论的是如何最简单的部署Flask。

项目的manage.py

	#!/usr/bin/env python3
	# coding:utf-8
	from flask.ext.script import Manager
	config = 'development'
	application = create_app(config)
	manager = Manager(application)
	...
	if __name__ == '__main__':
	  manager.run()
#新建uwsgi.ini文件
	[uwsgi]
	socket = 127.0.0.1:5000
	processes = 4
	threads = 2
	module = manage
	callable = application

配置参数说明：

	module：加载指定的python WSGI模块
	callable：在收到请求时，uWSGI加载的模块中哪个变量将被调用，默认是名字为“application”的变量.也是create_app的实例

#配置nginx的反向代理

nginx 的配置文件时位于 /etc/nginx/sites-available 目录下的 default 文件，我们复制一份做修改，这里同样给一份最简单的配置：

	server {
	  listen 80;
	
	  server_name 127.0.0.1;
	
	  # access_log logs/access.log compression;
	
	  #默认请求
	  location / {
	          include uwsgi_params;
	          uwsgi_pass 127.0.0.1:5000;
	  }
	}



#nginx启动后，Flask项目的启动方式：

	启动
	uwsgi uwsgi.ini

	停止
	
	如果还在同一个shell中，我们可以直接按 Ctrl + C
	如果不在同一个shell中，可以这样结束掉 killall -9 uwsgi

启动成功之后就可以访问我们的Web应用了，默认地址是：http://127.0.0.1:5000 （这个地址和端口号是在我们的Flask应用中配配置的，这里不做介绍）。

>需要特别说明的：
>
如果出现 invalid request block size: 21573 (max 4096)...skip这个错误，请将ini配置中的 socket 改为 http
