  Python中内置了很多有用的数据结构,列表list , 集合set,字典dict.那今天我们就根据这几个数据结构来看看python中 \* 的用法。\*的作用，如果在函数参数中\*表示的是不限的位置参数。*args,\*\*kwargs则说明了python中函数的动态赋值用法。

#python中的数据分解

####python2.x的写法

1.先看一个简单的例子

	a,b,c,d='wang'

	print a,b,c,d

显示的结果为：
>w a n g

  这说明了字符串“wang”对应的四个字符，自动被分解为 w ,a ,n ,g 给对了对应的变量


2，再看python中元祖的自动的分解

	a, b= ("name", 45)

	print a,b

显示的结果为：
>name 45

3，复合型元祖的做法

	a, b, (c, d) = ("a", 1, ("name", 45))

	print a, b, c, d
显示的结果为：
> a 1 name 45

4，python中dict 的分解

	a, b, c = {"name": "wangjing", "sex": "mal", "addrList": [u'湖北', u'湖南']}

	print a, b, c
显示的结果为 : 
>addrList name sex


_**说明python对已知长度的数据，可以做很好的自动分解,针对dict取到的是key**_

####python3.x的写法

对不知道长度的数据做了动态分解

	a,*b ,c='wangjing'
	print a ,b ,c
	
显示的结果为：
>w angjin g 


_**也就是说字符串wangjing，把首位赋值给了a,c ,把其它不知长度的值都给了b**_

#python中的动态传参

python中当函数的参数不确定时，可以使用*args 和**kwargs，*args 没有key值，**kwargs有key值

1,*args的用法

	def fun_args(pram, *args):  
    	print pram  
    	for value in args:  
        	print "another arg:", value  
  
	fun_args(1, 'wang', 3,'jng') # *args可以当作可容纳多个变量组成的list
显示的结果为：
>1  
>another arg: wang
>another arg: 3  
>another arg: jing

2，**kwargs的用法

	def fun_var_kwargs(farg, **kwargs):  
	    print "arg:", farg  
	    for key in kwargs:  
	        print "another keyword arg: %s: %s" % (key, kwargs[key])  
  
  
	fun_var_kwargs(farg=1, myarg2="two", myarg3=3)

myarg2和myarg3被视为key， **kwargs可以当作容纳多个key和value的dictionary  

显示结果为：
>arg: 1  
>another keyword arg: myarg2: two  
>another keyword arg: myarg3: 3 

3，与1同理的做法，对元祖自动分解，然后赋值

	re = ('wangjing',True)

	def fuc(a, b):
	    print a, b
	
	fuc(*re)
显示结果为：
>wangjing True

尾记：

>针对python中数据结构更加详细的用法，可以直接进官网查看<https://docs.python.org/3/>,这个是python3.x的用法
