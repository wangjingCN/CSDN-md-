#python中logging实现日志自动按日期分类
##日志功能的简单实现：
	#import logging
	logging.basicConfig(filename='logging.log', filemode='a',level=logging.DEBUG,format='%(levelname)s:%(asctime)s %(messages',datefmt='%Y-%m-%d %H:%M:%S')
	logging.info("info message")
显示的结果为：
>INFO:2016-11-01 17:47:24 info message

basicConfig的参数解释：

**filename 指的是，把日志输出到对应的文件里面**

**level 代表的是日志的级别：**
>
	logging的源码中一定定义了5种，日志级别：
	CRITICAL = 50
	ERROR = 40
	WARNING = 30
	INFO = 20
	DEBUG = 10

>对应的是logging的5种调用方法,debug（）、info（）、warning（）、error（）和critical（）
>只有当方法的级别不低于level时，才能显示

**format 分别指的是，把日志文件的输出格式**
**datefmt指format中时间的格式**
##日志功能的logger实现：
	#import logging
	logger = logging.getLogger()
	logger.setLevel(logging.DEBUG)
	logger_format = logging.Formatter(fmt='%(levelname)s:%(asctime)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
	
	logger_fh = logging.FileHandler('logging.log')
	logger_fh.setFormatter(logger_format)
	logger.addHandler(logger_fh)
	logger.info('logger info')

**这里实现了和上面同样的功能，定义的内容和上面也是一样.不同的是logger的使用**
![logger的实现方式](http://static.oschina.net/uploads/img/201509/21150840_RxZ9.png)

需要说明的是

	创建一个handler，用于写入日志文件    
	fh = logging.FileHandler('/tmp/test.log')  
  
	再创建一个handler，用于输出到控制台    
	ch = logging.StreamHandler() 
##日志进阶—：通过logger的方式，实现日志自动按月生成文件夹，并按照日期生成日志文件

	import logging
	import time
	import os
	def make_dir(make_dir_path):
	    path = make_dir_path.strip()
	    if not os.path.exists(path):
	        os.makedirs(path)
	    return path

	project_name = "Flask_web_log"
	folder_format = time.strftime('%Y-%m', time.localtime(time.time()))
	log_file_name = project_name + time.strftime('%Y-%m-%d', time.localtime(time.time())) + '.log'
	log_file_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir)) + os.sep + project_name + os.sep + folder_format
	make_dir(log_file_folder)
	log_file_str = log_file_folder + os.sep + log_file_name
	
	logger = logging.getLogger()
	logger.setLevel(logging.DEBUG)
	logger_format = logging.Formatter(fmt='%(levelname)s:%(asctime)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
	
	logger_fh = logging.FileHandler(log_file_str)
	logger_fh.setFormatter(logger_format)
	logger.addHandler(logger_fh)
	
	logger.info('实现了日志的自动分类')

最后自动生成的日志为以下结构：
	<li>Flask_web_log</li>
	<ul> 2016-11
	<ul>Flask_web_log2016-11-01.log</ul>
	</ul>
	<ul> 2016-12
	<ul>Flask_web_log2016-12-01.log</ul>
	</ul>