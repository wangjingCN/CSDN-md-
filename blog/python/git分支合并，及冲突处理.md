写的有点乱，只是做了一个总结

#分支操作,这里用test表示新的分支

##如何新建分支并切换到分支：	

	方法一：git checkout -b test

	方法二：git branch test
		   git checkout test

##如何查看当前分支

	git branch

显示结果为：

	*master
	test

***代表当前所在的分支，说明在主分支master下**
##如何查看远端分支
	git branch --romote
##合并test分支到master下

	第一步：先切换到master下面
			git checkout master
	第二部：git merge --no-ff test

合并分支时，可能遇到的问题：

	Auto Merge Failed; Fix Conflicts and Then Commit the Result.

处理办法：

	查看状态：git status，提示要git add,git commit ,
	一切完毕后，重新执行一次 git merge --no-ff test

#针对单个文件进行pull的方法：
	git fetch
	
	git checkout origin/master -- path/to/file
#版本回退的问题

	第一步：git reflog 
	#查看 commit日志,找到commit id
	
	第二部：git reset --hard id
	#回退到某个版本下
	

#冲突解决
##相同分支:
	首先：git pull
	然后：git add ,git commit ,git push
##不同分支
	首先：git merge branch 
	然后:git add ,git commit ,git push 	
	