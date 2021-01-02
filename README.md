# Homework2.0
 分布式系统和云计算
## （一）虚拟机服务器
### 一 本地虚拟机
0 配置虚拟机
1 设置虚拟机网络链接方式为桥接网卡后，开机运行。在命令行输入ifconfig命令后，得知虚拟机的IP地址为10.196.11.243。
![a](https://raw.githubusercontent.com/SYC-2357/Homework2.0/main/picture/a.png)

2 在本机的命令行中使用ipconfig命令查询IP地址为：10.196.8.203
![2](https://raw.githubusercontent.com/SYC-2357/Homework2.0/main/picture/2.png) 

3 在本机中使用ping连通虚拟机。
![4](https://raw.githubusercontent.com/SYC-2357/Homework2.0/main/picture/4.png)

4 将示例的HTML文件通过clone导入虚拟机
>git clone https://github.com/zxuqian/html-css-examples.git

导入后进入存储这个文件的目录后，输入
>python3 -m http.server

虚拟机开始作为服务器运行。
![5](https://raw.githubusercontent.com/SYC-2357/Homework2.0/main/picture/5.png)

5 在本机电脑的浏览器上输入虚拟机的IP地址访问，出现示例的页面，虚拟机服务器被正常访问，服务器显示访问记录。
![6](https://raw.githubusercontent.com/SYC-2357/Homework2.0/main/picture/6.png)
![7](https://raw.githubusercontent.com/SYC-2357/Homework2.0/main/picture/7.png)

### 二 附加题 阿里云虚拟机
1 在阿里云的控制台中创建实例，创建成功后就拥有了按照创建要求分配的云服务器，打开实例的交互命令台。
2 使用ifconfig可以查询云服务器的地址，但根据阿里云在服务器详情界面展示的外部IP地址为8.130.28.5。
![8](https://raw.githubusercontent.com/SYC-2357/Homework2.0/main/picture/8_.png)

3 使用ipconfig查询本机的IP地址，云服务器与本机相互使用ping命令确认连接。
![9](https://raw.githubusercontent.com/SYC-2357/Homework2.0/main/picture/9_.png)

4 使用命令
>python3 -m http.server 3389 

使服务器开始运行,端口号为3389
5 在本机电脑的浏览器上输入云服务器的外部IP地址访问，出现页面，服务器被正常访问，并显示访问记录。
![11](https://raw.githubusercontent.com/SYC-2357/Homework2.0/main/picture/11_.png)
![10](https://raw.githubusercontent.com/SYC-2357/Homework2.0/main/picture/10_.png)

6 注册个人域名 syc2357.xyz 
7 创建实例 IP地址为？？？？？？（使用了一个新实例）
8 在阿里云的域名管理器中使用域名解析将域名与实例的IP地址进行关联。
![13](https://raw.githubusercontent.com/SYC-2357/Homework2.0/main/picture/13.png)

9 使用命令
>python3 -m http.server 3389 

使服务器开始运行,端口号为3389
10 在本机电脑的浏览器上输入syc2357.xyz访问，出现页面，服务器被正常访问，并显示访问记录
![12](https://raw.githubusercontent.com/SYC-2357/Homework2.0/main/picture/12.png)
![1305](https://raw.githubusercontent.com/SYC-2357/Homework2.0/main/picture/1305.png)

**遇到的问题和解决办法**
1 本机无法ping通云服务器
>云服务器的IP地址是阿里云提供的地址，而不是使用ifconfig命令获得的。
解决这个问题可以通过本机ping连接上其他节点的IP地址来逐步寻找问题的具体地点。

2 云服务器开始服务后本机无法连接
>阿里云只开放了云服务器的部分端口号，未开放的端口号开使的服务无法被连接。可以更换为开放的端口号或者在实例管理中新添加所需的端口号。



## （二）Django

### 一 创建文件夹

### 二 案例news
1 创建mysite
2 创建news app
3 更改 mysite/news/models.py 创建数据库关系
4 在 setting 中增加 ‘news’
5 在mysite目录下使用命令sqlite3，管理数据库
  >.open db.sqlite3
  >.tables
  >.quit

6 更新数据库设置内容
>python manage.py makemigrations
>python manage.py migrate

7 创建数据库的管理员
>python manage.py createsuperuser

8 开始运行
>python manage.py runserver

运行后，访问 http://127.0.0.1:8000/admin 管理数据

9 新建news/url.py文件编辑url路径，在views中添加函数将可视化页面与数据关联起来，在templates中加入可视化页面的模板
10 访问http://127.0.0.1:8000/news/articles/2020 就可以查询2020年的新闻

### 三 更改案例news为作业上交平台
1 在models中更改class，创建新的class：Student Homework，设置class的数据格式
2 在admin中加入新的表名称
3 使用命令更新数据库
>python manage.py makemigrations

4 在templates目录下创建HTML文件，内容为提交作业的可视化界面格式
5 在views中创建class，将新的数据库models和HTML文件以及在页面中出现的选项关联起来
6 在url中添加path
>path('hw/create/', views.HomeworkCreate.as_view())

7 可以通过 http://127.0.0.1:8000/news/hw/create/ 链接访问用户页面
![14](https://raw.githubusercontent.com/SYC-2357/Homework2.0/main/picture/14.png)
