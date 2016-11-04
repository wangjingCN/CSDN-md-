#python中property的用法
python中属性函数property，可以使用@property来属性重构
##用@property来重构getter,setter方法

**首先来看看直接定义类属性的写法:**

	class Student(object):
	    pass
	
	
	student = Student();
	student.score = 5
	
	print student.score
>这样写有个问题：属性是直接暴露的，这样就不能对属性做检查设置

**那么我们对上面的程序进行getter和setter方法的改进，达到属性检查的目的**

	class Student(object):
    def get_score(self):
        return self._score

    def set_score(self, score):
        if score > 100 or score < 0:
            raise ValueError('score must be an integer!')
        self._score = score


	student = Student();
	student.set_score(102)
	print student.get_score()
>这样写就可以限制score：要大于0小于100

**上面的写法对Python来说复杂化，并且可读性变差，那我们用@property来重构**

	class Student(object):
	    @property
	    def score(self):
	        return self._score
	
	    @score.setter
	    def score(self, score):
	        if score > 100 or score < 0:
	            raise ValueError('score must be an integer!')
	        self._score = score
	
	
	student = Student();
	student.score = 90
	print student.score
>这样写达到了getter和setter同样的目的，但是更加简洁