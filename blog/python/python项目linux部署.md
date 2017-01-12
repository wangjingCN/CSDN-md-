#secauto3项目linux部署
	说明：此文档说明的是linux物理机的uwsgi+nginx的python方案
##第一步：pypi包的准备和安装
>项目中采用pip freeze > requirements.txt,生成所有的项目的python包,并下载
>
>以下为安装步骤：

	1.1 安装 Werkzeug
	1.2 安装 Jinja2
	1.3 安装 MarkupSafe
	1.4 安装 itsdangerous
	1.5 安装 click
	1.6 安装 Flask
	1.7 安装 WTForms
	1.8 安装 Flask-WTF
	1.9 安装 IPy
	1.10 安装 reloon
	1.11 安装 ptyprocess
	1.12 安装 pexpect
	1.13 安装 cryptography
	1.14 安装 idna
	1.15 安装 pyasn1
	1.16 安装 six
	1.17 安装 enum34
	1.18 安装 ipaddress
	1.19 安装 pycparser
	1.20 安装 cffi
	特别说明：离线安装时很容易出现‘command 'gcc' failed with exit status 1’错误
	解决办法：yum install gcc libffi-devel python-devel openssl-devel
	1.21 安装 paramiko
	1.22 安装 aniso8601-1.2.0.tar.gz
	1.23 安装 python-dateutil-2.6.0.tar.gz
	1.24 安装 pytz-2016.10.tar.gz
	1.25 安装 Flask-RESTful-0.3.5.tar.gz
	1.26 安装 Flask-Admin
	1.27 安装 Flask-Login
	1.28 安装 SQLAlchemy
	1.29 安装 Flask-SQLAlchemy
	1.31 安装 Mako-1.0.6.tar.gz
	1.32 安装 python-editor-1.0.3.tar.gz
	1.33 安装 alembic-0.8.9.tar.gz
	1.34 安装 Flask-Script-2.0.5.tar.gz
	1.35 安装 Flask-Migrate-2.0.2.tar.gz
	1.36 安装 Flask-HTTPAuth-3.2.1.tar.gz 
	1.37 安装 uwsgi
	1.38 安装 setuptools
	1.39 安装 netshell
	1.40 安装 pycrypto
	1.41 安装 pymysql

##第二步：mysql的yum安装和配置
	2.0 rpm -qa | grep mysql查看是否安装了数据库
	2.1 rpm -e --nodeps mysql卸载安装了的mysql数据库
	2.1.yum install mysql
	2.2.yum install mysql-server 
	2.3.yum install mysql-devel
	2.4 mysql配置文件/etc/my.cnf中加入default-character-set=utf8 
	2.5 service mysqld start 
	2.6 启动服务之后直接 mysqladmin -u root password 123456
	2.7 root登录数据库，让后 create secauto3数据库
	2.8 用database.sql来生成对应的数据库和表数据

**1./etc/my.cnf 这是mysql的主配置文件，2./var/lib/mysql   mysql数据库的数据库文件存放位置3日志，less /var/log/mysqld.log**

**需要特别说的是：如果是用客户端来连接，需要开通远程连接的权限**

grant select, update, delete, create on PICARRO.* to root@192.168.1.1    	identified by '123456';

	MySQL>use mysql 
	MySQL>update user set host = '%' where user = 'root'; 
	MySQL>select host, user from user; 
	MySQL>quit 
	MySQL>GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY 'mypassword' WITH GRANT OPTION；
	MySQL>FLUSH PRIVILEGES；
	MySQL>quit
**忘记密码：mysqld_safe –skip-grant-tables &**

	如先输入mysql,成功启动后输入use mysql,出现如下错误：Access denied for user ''@'localhost' to database 'mysql' 
	还有，输mysql可以，输mysql -u root就出错了：
	Access denied for user 'root'@'localhost' (using password: NO).
	The reason is:
	是昨日更新ROOT密码时出错
	update user set password = '123456' where user ="root" //这样写是错的，密码其实不是123456
	应该为update user set password = password ('123456') where user = "root"
	具体操作步骤：
	关闭mysql:
	# service mysqld stop
	然后:
	# mysqld_safe --skip-grant-tables
	启动mysql:
	# service mysqld start
	mysql -u root
	mysql> use mysql
	mysql> UPDATE user SET Password=PASSWORD('xxx') WHERE user='root';
	mysql> delete from user where user='';
	mysql> flush privileges;
	mysql>\q
##第三步：项目的配置
3.1**修改项目中config.py的数据库连接部分**

	class DevelopmentConfig(Config):
	    DEBUG = True
	    SQLALCHEMY_ECHO = False
	    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or "mysql+pymysql://root:123456@127.0.0.1/secauto3"

**3.2.配置uwsgi.ini文件：**

	[uwsgi]
	socket = 127.0.0.1:5000
	processes = 4
	threads = 2
	module = manage
	callable = application

**3.3.配置uwsgi.ini文件：**

	uwsgi uwsgi.ini

##第四步：nginx的安装和配置

**配置nginx的反向的代理**
>nginx 的配置文件时位于 /etc/nginx/sites-available 目录下的 default 文件

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
	