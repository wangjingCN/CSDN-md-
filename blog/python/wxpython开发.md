#用python进行桌面程序开发(GUI)，开发环境搭建

本主要是介绍开发软件和下载地址，具体安装和使用，请移步度娘。

##**第一步：安装python**
	
>安装地址：<http://www.python.org/download/>

##**第二步：安装pycharm(python IDE开发工具)**
	
>安装地址：<http://www.jetbrains.com/pycharm/download/#section=windows>

##**第三步：安装wxPthon 和demo**
	
>安装地址：<https://www.wxpython.org/download.php>

##**第四步：安装py2exe**
	
>安装地址：<http://www.py2exe.org/>

##**第五步：wxPython程序 用py2exe进行打包**

	from distutils.core import setup
	import py2exe
	includes = ["encodings", "encodings.*"]
	options = {"py2exe":
	             {   "compressed": 1,
	                 "optimize": 2,
	                 "includes": includes,
	                 "bundle_files": 1
	             }
	           }
	setup(
	     version = "0.1.0",
	     description = "windows program",
	     name = "winsetup",
	     options = options,
	     zipfile=None,
	     windows=[{"script": "myscript.py", "icon_resources": [(1, "PyCrust.ico")] }],
	  )

最后：运行windows命令行，运行如下代码：
	
	python setup.py py2exe

可能会报错：

	error: MSVCP90.dll: No such file or directory
	是因为没有找到MSVCP90.dll，在windows目录下搜索MSVCP90.dll这个文件，然后拷到python安装目录的DLLs下就可以了。

会产生build和dist文件夹。build里是一些py2exe运行时产生的中间文件，可以删除；只需将dist文件夹拷走就行，运行文件是app.exe，可以改名

	附：众所周知的墙，很多地址在公司是不能直接访问的。可以去的csdn 博客下载
	资源地址：<http://download.csdn.net/detail/u010445540/9633619>
