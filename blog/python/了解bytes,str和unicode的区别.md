#了解bytes,str和unicode的区别
首先来说把Unicode转换为为原始8位值（二进制数据），有很多种办

编写Python程序的时候，核心部分应该用Unicode来写，也就是python3中的str,python2中的unicode
##python3中2种表示字符序列的类型：bytes和str
前者的实例包含了原始8位值，后者的实例包含了Unicode字符

python3中接受bytes和str,并总是返回str：

	def to_str(bytes_or_str):
    	if isinstance(bytes_or_str, bytes):
        	return bytes_or_str.decode('utf-8')
    	return bytes_or_str

python3中接受bytes和str,并总是返回bytes：

	def to_bytes(bytes_or_str):
	    if isinstance(bytes_or_str, str):
	        return bytes_or_str.encode('utf-8')
	    return bytes_or_str

##python2中2种表示字符序列的类型：unicode和str
与python3刚好相反：后者的实例包含了原始8位值，前者的实例包含了Unicode字符

python2中接受unicode和str,并总是返回unicode：

	def to_str(bytes_or_str):
	    if isinstance(bytes_or_str, str):
	        return bytes_or_str.decode('utf-8')
	    return bytes_or_str

python2中接受unicode和str,并总是返回str：

	def to_bytes(bytes_or_str):
	    if isinstance(bytes_or_str, unicode):
	        return bytes_or_str.encode('utf-8')
	    return bytes_or_str

##python2和python3需要注意的事情

1.python2中如果str只包含7位的ASCII字符，那么unicode和str 就是同一种类型，可以+操作

2.python3内置的open函数获取文件句柄，默认采用utf-8的格式操作文件,python2则默认是二进制

>python2 的写法:
>
	with open（"/temp/file.bin",'w'）as f :
		f.write(os.urandom(10))

>python3 的写法:
>
	with open（"/temp/file.bin",'wb'）as f :
		f.write(os.urandom(10))
ps:如何让你的代码pythonic