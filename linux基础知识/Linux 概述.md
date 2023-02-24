# Linux 概述

## 1、系统文件

bin：二进制可执行文件

dev：外部挂载文件，键盘鼠标etc

home：用户不同的家目录

lib/lib64:加载时的动态库

media/mnt：挂载外部设备

proc/run:操作系统用

tmp：临时文件

usr：unix system resource Unix 系统资源

boot：开机启动项

etc：存储配置文件目录

opt：安装第三方软件目录

var：系统中经常会发生变化的文件

lost+found：非正常关机，存储临时文件，做系统恢复用

## 2、绝对路径和相对路径

相对路径：

./ 表示当前所在的目录

../ 表示当前目录的上层目录



绝对路径：

从系统的磁盘节点开始描述的路径

/root/luffy/get/..



## 3、命令提示行快捷键

ctrl+a：快速移动到命令行首部

ctrl+e：快速移动到命令行尾部

ctrl+u：删除光标前的字符串

ctrl+k：删除光标后的字符串



## 4、 文件信息

‘‘-’’ 为普通文件   白色

‘‘d’’为目录  蓝色

‘‘l’’为软连接文件  淡蓝色 青色 

‘‘c’’为字符设备文件  黄色

‘‘b’’为块设备文件 黄色

‘‘p’’为管道文件 棕黄色

‘‘s’’为套接字文件  粉色





## 5、用户类型

用户A ： 创建组A

用户B：  创建组B

文件的操作权限

读文件，写文件，执行权限，无权限

​     r             w              x               -

   read      write       excute      none(-)





## 6、创建目录

1、创建单层目录：

mkdir hello

mkdir hello/world 

还是创建了在hello 里面的world 文件夹



2、创建多层目录

mkdir -p a/b/c/d

在a 中 创建 b 在 b 中创建 c 在c 中创建d



tree **命令是调用树状文件设置**

rm -rf ./*



## 





## 7、touch命令

touch命令是用来创建文件夹的命令，

如果有这个文件夹，那么touch命令就会更新文件夹的事件

如果没有这个文件夹，那么touch命令就会创建一个文件夹出来



## 8、重定向

重定向只有两个符号：第一个是> ;第二个是 >>



第一个符号的意思是更新文件

```
echo daksdashdl > temp;
//意思是：将temp文件中的数据 用上面的数据覆盖掉，之前temp里面的数据就没有了
echo hsakdhah >> temp
//意思是：往temp文件中追加数据，之前temp文件中的数据还有，但是用以上的数据对temp文件进行一个追加操作
```





## 9、adduser命令

sudo adduser xxxx(用户名称)



然后可以使用sudo - han1(举例子，用户名称叫han1)

然后输入han1的密码即可切换到han1这个用户上面



推荐使用adduser，useradd比较麻烦





## 10、 userdel命令

通用的userdel命令

sudo userdel 用户名 -r



## 11、压缩和解压缩命令

1、tar 打包工具

linux不可以对所有的文件进行打包和压缩在一起的方法，只可以进行先打包再压缩的方法

tar就是打包工具，gzip和bzip2就是压缩工具，通常他们会一起工作





语法：tar 参数 生成压缩包的名字 要压缩的文件和目录

参数明细：

1、c 创建压缩文件

2、z 使用gzip进行压缩

3、j 使用bzip2进行压缩

4、v 压缩过程中显示相关信息

5、f 指定压缩包的名字



注：在生成压缩包的时候，为了方便识别，需要使用后缀作为区分

.tar.gz  ----> 先用tar进行打包，再用gzip进行压缩

.tar.bz2  ----> 先用tar进行打包，再用bzip2进行压缩



## 12、解压缩命令

语法是：

tar 参数 需要解压缩的压缩文件

参数明细：

1、x 解压缩工具

2、z 使用gzip工具进行解压缩

3、j 使用bzip2工具进行解压缩

4、v 解压缩时候显示信息

5、f 解压缩之后的文件名称



注：如果想要解压缩到响应的文件夹中，需要有参数 -C ，语法变成

tar 参数 需要解压缩的文件夹  -C  指定的文件夹目录



## 13、搜索命令 find

1、find  

1. 基于文件名称进行的搜索

语法： find 搜索路径 -name 要搜索的文件名称

例如：find ./ -name main.cpp 在全局搜索 main.cpp文件 

ex：搜索是递归的，所以速度可能会慢一些



2. 基于文件类型进行搜索

基本语法：find 搜素路径 -type 文件类型

注：在linux中的文件类型有七种

f  普通类型文件   file

d 目录文件 direction

l 软连接文件 link

c 字符类型文件 character

b 快文件 block

p 管道文件 path

s 网络连接字文件 socket



模糊搜索：通配符 * ？

这俩通配符可以匹配零个或任意的多个的字符

ex：find ./ -name     '*.cpp'

**注意：一定得加引号，单引号或者双引号**





3. 基于文件大小进行搜索

基本语法：find 搜索路径 -size 【+|-】文件大小

例子：

-size 4k 区间是3k - 4k  (3k-4k]

**-size -4k   0 --- 3k**  [0-3k)

-size +4k 4k ---- 无穷 (4k- 无穷)

-k 

-M 

-G 





 

## 14、搜索函数 grep

搜索语法:

grep “搜索内容”  搜索路径 / 文件   参数



语法格式：grep “搜索内容”  搜索路径/文件 参数

参数：-r 搜索目录中的文件内容

​			-i 搜索对应关键字，忽略大小写的差别

​			-n 列出符合样式的行编号





##  

## 15、搜索函数locate

基于文件名称进行查找

是一个简化版的find





## 16、gcc和g++

gcc和g++都可以编译c or c++ 文件

不同的在于g++可以调用gcc来编译

gcc就是自己编译即可

用gcc 编译.c文件时，基本语法

**gcc 文件名称.c -o 可执行文件名称**



用gcc编译.cpp文件时，基本语法

**gcc 文件名称.cpp -o 可执行文件名称 -lstdc++**

注：后面的这个 -lstdc++一定要加上，不然用从gcc编译.cpp文件会报错







## 17、静态库

静态库：前缀 lib 后缀.a 中间是自己制定的名字

例如：libxxxx.a

1. 生成静态库

生成静态库需要先对源文件进行汇编操作（使用参数-c），得到二进制目标文件.（o格式），然后在通过ar工具将目标文件打包就可以得到静态文件库了（libxxx.a）



参数c:创建一个库，不管这个库是否存在 （-create） 

参数r:在库中间插入模块（替换）。默认新的成员添加在库的结尾处，如果模块名称已经存在，则替换同名的模块 （-replace）

参数s:创建目标文件的索引，在创建较大的库中比较节省事件



![](/home/han/Pictures/Screenshot from 2023-02-22 18-02-26.png)







1、需要将源文件进行汇编，得到.o 文件，需要使用参数-c

gcc -c 源文件.c



2、将得到的.o文件进行打包，得到静态库 **（使用到了gcc中的ar打包文件）**

ar rcs 自己起的静态库的名称（ex：libxxx.a） 原材料.o文件（上一个步骤生成的.o文件）



3、发布静态库

提供制作的头文件 head.h

提供制作出来的静态库 libxxx.a





2. 使用静态库

生成的静态库的名字是libxxx.a，但是再使用静态库的过程当中需要进行掐头去尾 也即在使用libxxx.a 库的时候，只需要指定参数xxx即可



3. 使用libxxx.a库中的函数来编译main.c文件

gcc main.c -o main -L ./ -l xxx

解释：gcc main.c -o main 这就不用说了

-L ：指定的是使用库的具体路径 上述例子中的./ 指的是当前的目录下

-l ：指定的是使用库的具体名字，需要对静态库进行掐头去尾 剩下中间的名字（也就是自己编写的库函数的名字即可）



## 18、动态库

以lib为前缀，以.so为后缀 -------> linux

以lib为前缀，以.dll为后缀 ------->windows



静态库中的代码会放在代码区， ------> 绝对地址

动态库放在动态库加载区。---------> 相对地址



语法格式：

1. 将源文件进行汇编操作（注意，必须要添加额外的参数 -fpic）

​	ex：gcc -c **-fpic**  *.c(源文件)



2. 将上述的*.o文件进行打包，生成动态库 (需要使用 -shared 参数和 gcc 进行打包)

​	ex：gcc -shared 上述的 *.o -o 动态库的名字（libxxx.so）



使用动态库的方法和使用静态库一样

语法格式：gcc (要编译的源文件 ex：main.c) -o (生成的二进制执行文件)     -L   (动态库的路径)   -l (动态库掐头去尾的名字 -------> 也就是自己给起的名字)



这时候，可能会出现报错，提示找不到动态库

```c
$ error while loading shared libraries: libcacl.so: cannot open shared object file: No such file or directory
```



说明没有找到动态库，这是为什么呢？

原因：

1. 没有该动态库（这时候应该去寻找所所需要的动态库）
2. 动态库没有被加载到内存中。这时候，就需要动态载入器来获取该动态库的绝对路径

way1：当前用户级别的配置  vim ~/.bashrc     在最后一行加上 

```vim
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/home/han/calculator/dynamic_lib
```

然后关闭当前终端，重启一个终端即可



way2：系统级别配置 vim /etc/profile

也是添加上述代码对LD_LIBRARY_PATH进行配置

然后注销或者关机，再次开机则配置生效





## 19、动态库和静态库的区别

**静态库**被打包，加载速度快

发布程序无需提供库文件，移植方便



但是；

文件数据被加载了多份，浪费资源；还需要编译多分资源，造成资源浪费



**动态库** 可以直线不同进场之间的资源共享

动态库升级简单，只需要替换库文件，无需重新编译程序





## 20、Makefile图纸

make 命令的图纸 就是 Makefile

 基本语法结构：

target1，target2..... : depend1,depend2,....

(要加一个tab键)	command1

​								command2

​								。。。。。

​								。。。。。



target就是生成的目标：例如生成可执行文件

depend：就是依赖，需要什么原材料

command：就是命令，怎样通过原材料生成目标

```makefile
# 举例: 有源文件 a.c b.c c.c head.h, 需要生成可执行程序 app
################# 例1 #################
app:a.c b.c c.c
	gcc a.c b.c c.c -o app

################# 例2 #################
# 有多个目标, 多个依赖, 多个命令
app,app1:a.c b.c c.c d.c
	gcc a.c b.c -o app
	gcc c.c d.c -o app1
	
################# 例3 #################	
# 规则之间的嵌套
app:a.o b.o c.o
	gcc a.o b.o c.o -o app
# a.o 是第一条规则中的依赖
a.o:a.c
	gcc -c a.c
# b.o 是第一条规则中的依赖
b.o:b.c
	gcc -c b.c
# c.o 是第一条规则中的依赖
c.o:c.c
	gcc -c c.c

```

  

可以使用Makefile文件中的变量，让Makefile更简洁



**内定义变量，预定义变量**，自动变量



1. **自定义变量：**

变量名 = 变量值

ex：abc = 123

如果要取出变量值，那么需要将变量名放在 $(     )这个结构当中

```makefile
obj = add.o sub.o div.o  mult.o   ##用变量名代替变量值

$(obj) ##取出变量值
```







2. **预定义变量**

![](/home/han/Pictures/Screenshot from 2023-02-23 12-48-45.png)



```makefile
## 普通写法：
calc:add.o sub.o div.o mult.o main.o
	gcc add.o div.o sub.o mult.o main.o -o calc
	
	
##使用变量的写法：
target=calc
obj=add.o sub.o div.o mult.o
CFLAGS=-o3 ##这是代码优化的例子。代码优化总共有三级， -O0 -O1 -O2 -O3
$(target):$(obj)
	$(cc) $(obj) -o $(target) $(CFLAGS)
```



3. **自动变量**

![](/home/han/Pictures/Screenshot from 2023-02-23 12-57-22.png)



ex：

```
calc:add.o sub.o mult.o div.o main.o
	gcc add.o sub.o div.o mult.o main.o -o calc
```



常用的自动变量有三个：

$@ : 指的是上述中的calc

$< : 指的是上述文件中的add.o

$^ : 指的是上述文件中的不依赖的项，在上述Makefile中 指的是 add.o sub.o div.o main.o mult.o





模板匹配：

使用了一个公式，代表若干个满足条件的规则：

```makefile
%.o : %.c
	gcc $< -c 
```

%的意思是通配符，意思通配依赖的文件名称

ex：add.o  -----> %.o      % = add

即可





## 21、Makefile中的函数

 介绍几个常用的函数 wildcard 和 patsubst

函数1：wildcard

获取指定目录下的文件名称，其中它的返回值是割裂的，指定目录下的所有符合条件的文件名列表





```makefile
# 该函数的参数只有一个, 但是这个参数可以分成若干个部分, 通过空格间隔
$(wildcard PATTERN...)
	参数:	指定某个目录, 搜索这个路径下指定类型的文件，比如： *.c
```

```makefile
ex:src = $(wildcard *.c ./sub/*.c) ##在当前文件夹中找后缀名称为.c的文件，在当前文件夹中的sub文件夹找所有后缀名为.c文件的文件
```

```makefile
#返回格式是：a.c b.c c.c d.c ./sub/a.c ./sub/b.c
```



函数2：patsubst函数 

功能：按照指定的模式替换指定文件的后缀名

```makefile
# 有三个参数, 参数之间使用 逗号间隔
$(patsubst <pattern>,<replacement>,<text>)

参数功能:
pattern: 这是一个模式字符串，需要指定出要被替换的文件名中的后缀是什么
文件名和路径不需要关心，因此使用 % 表示即可 [通配符是 %]
在通配符后边指定出要被替换的后缀，比如: %.c, 意味着 .c 的后缀要被替换掉
replacement: 这是一个模式字符串，指定参数 pattern 中的后缀最终要被替换为什么
还是使用 % 来表示参数 pattern 中文件的路径和名字
在通配符 % 后边指定出新的后缀名，比如: %.o 这表示原来的后缀被替换为 .o
text: 该参数中存储这要被替换的原始数据
返回值:
函数返回被替换过后的字符串。
```

```makefile
src = a.cpp b.cpp c.cpp d.cpp
#把变量中所有的后缀名从cpp改成o
obj = $(patsubst %.cpp , %.o , $(src))
#src中所有的cpp的文件，在obj中全变成了.o文件 
```



伪目标：让make忽略构建的时间戳

添加.PHONY函数

声明方式 ： .PHONY:伪文件名称

![](/home/han/Pictures/Screenshot from 2023-02-24 11-23-50.png)



即使内部文件中有clean这个文件，但是在构建如果忽略了时间戳的话，那么就不会报错







## 22、GDB 调试



之前学过了，觉得不如使用IDE 进行调试（可能也是我比较懒吧 ~乐~）

