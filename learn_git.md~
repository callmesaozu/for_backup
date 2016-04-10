Git is a vversion control system.
Git is free software.
>廖雪峰老师的官方网站
>http://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000

# 安装
`$ sudo apt-get install git`
# 设置全局变量名
`$ git config --global user.name"your Name"`
`$ git config --global user.email"yourEmail@example.com"`
表示这台机器上所有的git仓库都使用这个配置,便于同伴标识自己，也可以为每个仓库指定单独的名称
# 创建版本库
`$ mkdir /home/lord/git_repository`
`$ cd /home/lord/git_repository`
`$ pwd  #pwd命令用于显示当前目录`
`/home/lord/git_repository`
# 版本库的初始化
`$ git init`
`初始化空的 Git 版本库于 /home/lord/git_repos/.git/`
可发现当前路径下多了一个.git目录，这个目录不要动, 隐藏的，可用`ls -ah`查看

# 添加文件
- 要将文件拷贝到当前目录下
- 只能跟踪文本文件的内容
- word文件不行，是二进制文件
`$ git add test_git.txt`
`$ git commit -m"编写了一个文件，用来记录git的学习过程"`
```
$ git add file1.txt
$ git add file2.txt file3.txt
$ git commit -m"add 3 files"
```
# 修改
- 查看修改
`$ git status`
```
位于分支 master
尚未暂存以备提交的变更：
  （使用 "git add <file>..." 更新要提交的内容）
  （使用 "git checkout -- <file>..." 丢弃工作区的改动）

	修改:         test_git.txt

未跟踪的文件:
  （使用 "git add <file>..." 以包含要提交的内容）

	test_git.txt~

修改尚未加入提交（使用 "git add" 和/或 "git commit -a"）
```
- 查看具体修改内容
```
$ git diff
diff --git a/test_git.txt b/test_git.txt
index 5cef34a..66e4a88 100644
--- a/test_git.txt
+++ b/test_git.txt
@@ -1,2 +1,30 @@
 Git is a vversion control system.
 Git is free software.
+# 安装
+`$ sudo apt-get install git`
+# 设置全局变量名
+`$ git config --global user.name"your Name"`
+`$ git config --global user.email"yourEmail@example.com"`
+表示这台机器上所有的git仓库都使用这个配置,便于同伴标识自己，也可以为每个仓库指
+# 创建版本库
+`$ mkdir /home/lord/git_repository`
+`$ cd /home/lord/git_repository`
+`$ pwd  #pwd命令用于显示当前目录`
+`/home/lord/git_repository`
+# 版本库的初始化
+`$ git init`
+`初始化空的 Git 版本库于 /home/lord/git_repos/.git/`
+可发现当前路径下多了一个.git目录，这个目录不要动, 隐藏的，可用`ls -ah`查看
+
```
- 提交修改
```
$ git add test_git.txt
$ git commit -m"添加了一些修改命令"
```
`$ git add -A`添加所有文件
# 回退

- 回顾每次提交修改的内容
`$ git log`
commit事实上是一个文件快照，MD5?
`$ git log --pretty=oneline`
```
12b4a63dcc70cd521ce669ffed9bdf8c461ef592 添加了提交修改命令
a335aeecc09196d76ef52146239c328ce3d8d055 添加了一些修改命令
39397d606bf086bf1239988e3dec25fea0e7ac51 一个用于学习git命令的文件
0ac6e5b20f4304b55d39ba08b92398c78a5ff0b7 编写了一个文件，从movieLen的数据集中读
```
用于美化显示
`12b4a63dcc70cd521ce669ffed9bdf8c461ef592`之类的数字是commit id(版本号),通过SHA1计算得出，用16进制表示
- 退回到某个版本
`$ git reset --hard HEAD^`
-- HEAD是指当前版本
-- HEAD^之当前版本的前一个版本
-- HEAD^^............两个版本, HEAD^^^...
-- HEAD~100，当前版本的前100个版本
或者
`$ git reset --hard 12b4a63dc`
-- 12b4a63dc是要回到的版本的版本号的一部分，不必写全
- 查看当前版本的内容
`$ cat test_git.txt`
- 查看所有的版本号
`$ git reflog`

# 一些名词
- 工作区：电脑里能看到的目录， 如/home/lord/git_repos文件夹
- 版本库：工作区中的隐藏目录.git， 其中包含：
-- stage或者index的暂存区
-- git自动创建的第一个分支master
-- 一个指向master的指针HEAD

- git add事实上就是把文件修改添加到暂存区
- git commit是把暂存区的所有内容提交到当前分支

# 撤销修改
- `$ git checkout -- filename`用于撤销当前版本的修改, 但未add
- `git reset HEAD filename`用于把暂存区的修改撤销掉，unstage，从新放回工作区
-- `$ git reset`命令既可以回退版本，也可以把暂存区的修改回退到工作区
# 删除文件
- 如果一个文件提交到版本库中，可以用`$ git rm fordelete.txt`删除
-- 工作区中文件和版本库中一并删除
- 如果一个文件提交到版本库中，并且已经手动删除
-- 还可以用`$ git checkout -- fordelete.txt`命令恢复
-- 如果要彻底删除，则用`$ git rm -- fordelete.txt`
-- `checkout`命令是用版本库中的版本替换工作区的版本，无论工作区是修改还是删除，都可以一键还原

# 远程仓库
- 可以使用github，也可以自己搭建一个服务器
- 本地Git仓库和Github仓库之间的传输是通过SSH加密的
1. `$ ssh-keygen -t rsa -C "yourEmail@example.com"`
2. 一路回车:可发现在主目录下有一个.ssh文件，里面有两个文件.id_rsa和.id_rsa.pub
-- `ctrl+h`可以查看隐藏文件和文件夹
3. .id_rsa里是私钥，不能泄漏， .id_rsa.pub里是公钥，可以告诉任何人
4. 登录github，打开“Account settings”，“SSH Keys”页面
5. Add SSH key，填任意title，key文本框中粘贴id_rsa.pub中的所有内容
6. Add Key
7. 一个github账户可以添加多个key

# github上的远程库
1. 登录Github, create a new repository, name:"for_backup", create repository
2. `$ git remote add origin git@github.com:callmesaozu/for_backup.git`
-- 远程库的名字是origin，默认，可以改，但没必要
3. `$ git push -u origin master`
-- 把当前分支master推送到远程
-- 由于一开始远程库为空， 所以`-u`参数会把本地master分支和远程的master分支关联起来，用于以后的简化
-- 会出现SSH警告
```
The authenticity of host 'github.com (192.30.252.129)' can't be established.
RSA key fingerprint is 16:27:ac:a5:76:28:2d:36:63:1b:56:4d:eb:df:a6:48.
Are you sure you want to continue connecting (yes/no)?
```
这是因为SSH连接时需要确认github的key是否真的来自github服务器，输入yes，以后就不用了
4. 以后的操作： `$ git push origin master`

# clone from origin
- `git clone git@github.com:callmesaozu/gitskills.git`
- 也可以clone他人的repo
- 支持多种协议，但通过ssh支持的原生git速度最快

# 分支管理
- git鼓励大量使用分支
- 查看分支: `$ git branch`
- 创建分支： `$ git checkout -b dev`
-- 相当于两个命令
-- `$ git branch dev`
-- `$ git checkout dev`
-- 创建并转到dev分支
- 合并分支到当前分支： `$ git merge master #假设当前分支为master`
- 删除分支： `$ git branch -d dev`

## 分支冲突
- 当git无法自动合并时， 先手动解决冲突，在冲突的文件中会有如下显示
```
<<<<<<< HEAD
Creating a new branch is quick & simple.
=======
Creating a new branch is quick AND simple.
>>>>>>> feature1
```
- 解决冲突后正常提交
-- `$ git log --graph --pretty=oneline  --abbrev-commit`可以查看分支图形
## 分支管理策略

- 通常，合并分支时，如果可能，Git会用Fast forward模式，但这种模式下，删除分支后，会丢掉分支信息。
- 如果要强制禁用Fast forward模式，Git就会在merge时生成一个新的commit，这样，从分支历史上就可以看出分支信息。
- `$ git merge --no-ff -m"merge with no-ff" dev`, 可以保留dev分支的信息，因为要创建一个commit，所以要添加commit描述
- 几个注意点
-- *首先，master分支应该是非常稳定的，也就是仅用来发布新版本，平时不能在上面干活*

-- *干活都在dev分支上，也就是说，dev分支是不稳定的，到某个时候，比如1.0版本发布时，再把dev分支合并到master上，在master分支发布1.0版本*

## bug分支
- `$ git stash`冻结当前未提交的修改，用于debug
- 创建一个分支，在新分支上debug，然后提交
- 回到原分支， 合并新分支
- `$ git stash pop`, 恢复冻结的内容，同时删除stash内容，debug的结果也会提交
-- `$ git stash list`查看stash内容
-- 另一种方法用git stash apply恢复，但是恢复后，stash内容并不删除，你需要用git stash drop来删除

## feature分支
- 最好每添加一个新功能都新建一个feature分支，在feature分支上添加功能，最后再合并到原分支上
- 在合并之前，如果删除feature分支，将失掉修改，因此git会阻止这种行为
- 如果要强行删除，用`$ git branch -D feature`, 注意D是大写

## 多人协作
- `$ git remote`查看远程库的信息
-- 如果要详细的信息， 用`$ git remote -v`
- 推送分支可以用`$ git push origin branchName`
-- master是主分支，要时刻同步
-- dev是开发分支，所有成员都在上面工作，也需要同步
-- feature分支视具体情况而定
-- bug分支不需要
- 抓取分支
1. 假设当前的分支为dev，将其推送到远程库`$ git push origin dev`
2. 同伴在自己目录下克隆我的远程库`$ git clone git@github.com:callmesaozu/for_backup`
3. 同伴只能看到master分支，用`$ git checkout -b dev origin/dev`切换到dev分支
4. 假如同伴修改了文件readme, 在自己的本地库中提交更改以后，更新到远程库中，`$ git push origin dev`
5. 假如我也修改了readme文件，推送到远程库时可能推送失败
```
$ git push origin dev
To git@github.com:callmesaozu/for_backup.git
 ! [rejected]        dev -> dev (fetch first)
error: 无法推送一些引用到 'git@github.com:callmesaozu/for_backup.git'
提示：更新被拒绝，因为远程版本库包含您本地尚不存在的提交。这通常是因为另外
提示：一个版本库已向该引用进行了推送。再次推送前，您可能需要先整合远程变更
提示：（如 'git pull ...'）。
提示：详见 'git push --help' 中的 'Note about fast-forwards' 小节。
```
6. 用`$ git pull`将远程库中的文件克隆到本地，解决冲突后再提交
```
$ git pull
自动合并 readme~
冲突（内容）：合并冲突于 readme~
自动合并 readme
冲突（内容）：合并冲突于 readme
自动合并失败，修正冲突然后提交修正的结果。
```
如果`$ git pull`失败，一般是因为没有指定本地dev分支与远程origin/dev分支的链接，根据提示，设置dev和origin/dev的链接：
```
$ git pull
remote: Counting objects: 3, done.
remote: Compressing objects: 100% (1/1), done.
remote: Total 3 (delta 2), reused 3 (delta 2), pack-reused 0
Unpacking objects: 100% (3/3), done.
来自 github.com:callmesaozu/for_backup
   dfc06f6..1d382ce  dev        -> origin/dev
There is no tracking information for the current branch.
Please specify which branch you want to merge with.
See git-pull(1) for details

    git pull <remote> <branch>

If you wish to set tracking information for this branch you can do so with:

    git branch --set-upstream-to=origin/<branch> dev
$ git branch --set-upstream dev origin/dev
Branch dev set up to track remote branch dev from origin.
```
再git pull



