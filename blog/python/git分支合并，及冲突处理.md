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

##合并test分支到master下
	第一步：先切换到master下面
			git checkout master
	第二部：git merge --no-ff test

合并分支时，可能遇到的问题：

	Auto Merge Failed; Fix Conflicts and Then Commit the Result.

处理办法：

	查看状态：git status，提示要git add,git commit ,
	一切完毕后，重新执行一次 git merge --no-ff test
   
#提交冲突时候的解决办法
