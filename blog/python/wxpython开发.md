#用python进行桌面程序开发(GUI)，开发环境搭建

##**第一步：安装python**
	
>安装地址：<http://www.python.org/download/>


##**第二步：安装pycharm(python IDE开发工具)**
	
>安装地址：<http://www.jetbrains.com/pycharm/download/#section=windows>

##**第三步：安装wxPthon 和demo**
	
>安装地址：<https://www.wxpython.org/download.php>

##**第四步：安装boa-constructor 0.6.1**
	
>安装地址：<boa-constructor 0.6.1>

##**第五步：安装py2exe**
	
>安装地址：<boa-constructor 0.6.1>

##**第六步：wxPython开发的程序 用py2exe进行打包**

	from distutils.core import setup  
	import py2exe  
	setup(windows=[{"script": "app.py"}])

最后：运行windows命令行，运行如下代码：
	
	python convert2exe.py py2exe

会产生build和dist文件夹。build里是一些py2exe运行时产生的中间文件，可以删除；只需将dist文件夹拷走就行，运行文件是app.exe，可以改名。