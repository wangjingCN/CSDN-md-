#Flask_script在flask项目中manage.py的简单用法

##flask框架中manage.py的常用设计

	#!/usr/bin/env python
	import os
	from app import create_app, db
	from app.models import DBNSZone, DBNSDevice, DBNSLink, DBNSNSIPAssign, DBSYSDevice, DBSYSMenu, DBSYSUser, \
	    DBSYSUserMapMenu
	from flask.ext.script import Manager, Shell
	from flask.ext.migrate import Migrate, MigrateCommand
	
	app = create_app(os.getenv('FLASK_CONFIG') or 'default')
	manager = Manager(app)
	migrate = Migrate(app, db)
	
	
	def make_shell_context():
	    return dict(app=app, db=db, DBNSZone=DBNSZone,
	                DBNSDevice=DBNSDevice, DBNSLink=DBNSLink, DBNSNSIPAssign=DBNSNSIPAssign, DBSYSDevice=DBSYSDevice,DBSYSUserMapMenu=DBSYSUserMapMenu
	                )
	
	
	manager.add_command("shell", Shell(make_context=make_shell_context))
	manager.add_command('db', MigrateCommand)
	
	
	@manager.command
	def test():
	    """Run the unit tests."""
	    import unittest
	    tests = unittest.TestLoader().discover('tests')
	    unittest.TextTestRunner(verbosity=2).run(tests)
	
	
	@manager.option('-d', '-drop_first', dest='drop_first', default=False)
	def createdb(drop_first):
	    """Creates the database."""
	    if drop_first:
	        print 1
	        db.drop_all()
	    db.create_all()
	
	@manager.command
	def yes(name="Fred"):
	    print "hello", name
	
	
	if __name__ == '__main__':
	    manager.run()

项目主要是用了Flask_srcipt 的Manager类来进行命令行的管理.

##启动项目

**默认启动项目的方法**
>\>python manage.py runserver

	项目会以：Running on http://127.0.0.1:5000/ 的方式启动


**指定端口启动**
>\>python manage.py runserver -h 127.0.0.1 -p 204

	项目会以：Running on http://127.0.0.1:204/ 的方式启动,其实也是可以指定IP的，只是本质也是127.0.0.1

##通过Flask_script来初始化数据库
>\>python manage.py shell
>
>\>>>db.create_all()

同时也可以通过shell方法来调用数据库实例:

>\>python manage.py shell
>
>\>>>a=DBNSLink(id=1,name='jing')
>
>\>>>a.save()

##启动测试文件
>\>python manage.py test
>
	@manager.command
	def test():
	    """Run the unit tests."""
	    import unittest
	    tests = unittest.TestLoader().discover('tests')
	    unittest.TextTestRunner(verbosity=2).run(tests)
主要是通过@manager.command装饰器来定义了一个test方法

##Flask_script通过传参来控制Flask项目:

>\>python manage.py createdb -d True
>
	@manager.option('-d', '-drop_first', dest='drop_first', default=False)
	def createdb(drop_first):
	    """Creates the database."""
	    if drop_first:
	        print 1
	        db.drop_all()
	    db.create_all()

manage.py的yes方法也可以采用同样的传值方式：
>\>python manage.py yes -n jing

	注意：**-n 是由参数的第一个字母决定的。所以"name" > "-n"**

Flask_script插件的具体用法，下面的网址讲的很详细

Flask_script文档中文翻译：
[https://my.oschina.net/lijsf/blog/158828](https://my.oschina.net/lijsf/blog/158828 "Flask_script文档中文翻译")
