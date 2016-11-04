#Python中的迭代器iterator和yield生成器(constructor）
---

## 什么叫迭代器和可迭代对象？ 

###一、可迭代对象(Iterable)
可以直接作用于for循环的对象统称为可迭代对象(Iterable)。

所有的Iterable均可以通过内置函数iter()来转变为Iterator。

然后使用它的next()方法调用，直到监测到一个StopIteration异常。

	a = [1, 2, 3, 4]
	b = iter(a)
	print b.next()
	print b.next()
	print b.next()
	print b.next()
	print b.next()

显示结果为：

>	1
>	
>	2
>	
>	3
>	
>	4
>	
>	Traceback (most recent call last):
>	
>	File "C:/workspace2/secAuto_flask/test3.py", line 13, in <module>
>	
>	print b.next()
>	
>	StopIteration
###二、迭代器(iterator)
迭代器是一个实现了迭代器协议的对象，在Python中，支持迭代器协议就是实现对象的\__iter\__()和next()方法。其中__iter__()方法返回迭代器对象本身；next()方法返回容器的下一个元素，在结尾时引发StopIteration异常。

其实，当我们使用for语句的时候，for语句就会自动的通过__iter__()方法来获得迭代器对象，并且通过next()方法来获取下一个元素。

看看我们自定义的迭代器：

	class MyIterator(object):
	    def __init__(self, n):
	        self.index = 0
	        self.n = n
	
	    def __iter__(self):
	        return self
	
	    def next(self):
	        if self.index < self.n:
	            var = self.index
	            self.index += 1
	            return var
	        else:
	            raise StopIteration

for的调用方式：

	myRange = MyIterator(3)
    for i in myRange:
        print i
next的调用方式:

	myRange = MyIterator(3)
    print myRange.next()
    print myRange.next()
    print myRange.next()
这两种方式显示的结果：

>0
>
>1
>
>2


_**使用迭代器一个显而易见的好处就是：每次只从对象中读取一条数据，不会造成内存的过大开销**_

比如要逐行读取一个文件的内容，利用readlines()方法，我们可以这么写：


	for line in open("test.txt").readlines():
	print line


这样虽然可以工作，但不是最好的方法。因为他实际上是把文件一次加载到内存中，然后逐行打印。当文件很大时，这个方法的内存开销就很大了。

利用file的迭代器，我们可以这样写：

	for line in open("test.txt"):   #use file iterators
	print line

这是最简单也是运行速度最快的写法，他并没显式的读取文件，而是利用迭代器每次读取下一行。

##二、生成器(constructor)

生成器函数在Python中与迭代器协议的概念联系在一起。简而言之，包含yield语句的函数会被特地编译成生成器。当函数被调用时，他们返回一个生成器对象，这个对象支持迭代器接口。函数也许会有个return语句，但它的作用是用来yield产生值的。

不像一般的函数会生成值后退出，生成器函数在生成值后会自动挂起并暂停他们的执行和状态，他的本地变量将保存状态信息，这些信息在函数恢复时将再度有效

	def g(n):
		for i in range(n):
			yield i **2
	
	for i in g(5):
	 	print i,":",
显示的结果：

>0 : 1 : 4 : 9 : 16 :


要了解他的运行原理，我们来用next方法看看：

	t=g(5)
	print t.next()
	print t.next()
	print t.next()
	print t.next()
	print t.next()
	print t.next()

显示结果为：

>0
>
>1
>
>4
>
>9
>
>16
>
>Traceback (most recent call last):
>
>  File "<stdin\>", line 1, in <module\>
>  
>  StopIteration

在运行完5次next之后，生成器抛出了一个StopIteration异常，迭代终止。
再来看一个yield的例子，用生成器生成一个Fibonacci数列：


##利用yield从序列中移除重复项，切保存元素顺序不变

	def dedupe(items, key=True):
	    seen = set()
	    for item in items:
	        var = item if key else key(item)
	        if var not in seen:
	            yield item
	            seen.add(var)
	
	
	a = [1, 2, 6, 3, 2, 4, 5, 3, 6]
	b = list(dedupe(a))
	print b
