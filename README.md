# Homework2.0
 分布式系统和云计算
## 虚拟机服务器
### 本地虚拟机
1 设置虚拟机网络链接方式为桥接网卡后，开机运行。在命令行输入ifconfig命令后，得知虚拟机的IP地址为10.196.11.243。
![avatar](D:\inschool\分布式与云计算\1.png)
2 在本机的命令行中使用ipconfig命令查询IP地址为：10.196.8.203
![avatar](D:\inschool\分布式与云计算\2.png)
3 在本机中使用ping连通虚拟机
![avatar](D\inschool\分布式与云计算\4.png)
4 将示例的HTML文件通过clone导入虚拟机
>git clone https://github.com/zxuqian/html-css-examples.git
导入后进入存储这个文件的目录后，输入
>python3 -m http.server

虚拟机开始作为服务器运行
![avatar](D\inschool\分布式与云计算\5.png)
5 在本机电脑的浏览器上输入虚拟机的IP地址访问，出现示例的页面，虚拟机服务器被正常访问，服务器显示访问记录。
![avatar](D\inschool\分布式与云计算\6.png)
![avatar](D\inschool\分布式与云计算\7.png)

### 阿里云虚拟机
1 在阿里云的控制台中创建实例，创建成功后就拥有了按照创建要求分配的云服务器，打开实例的交互命令台。
2 使用ifconfig可以查询云服务器的地址，但根据阿里云在服务器详情界面展示的外部IP地址为8.130.28.55
3 使用ipconfig查询本机的IP地址，云服务器与本机相互使用ping命令确认连接
4 在本机电脑的浏览器上输入云服务器的外部IP地址访问，出现页面，服务器被正常访问，并显示访问记录。

## 云盘软件

### 创建云盘文件夹
吱吱吱吱在

### 案例news
1 创建mysite
2 创建news app
3 更改 mysite/news/models.py 创建数据库关系
4 在 setting 中增加 ‘news’
5 在mysite目录下splite3
  >.open db.sqlite3
  >.tables
  >.quit

6 python manage.py makemigrations
  python manage.py migrate
7 python manage.py createsuperuser
8 python manage.py runserver后，访问 http://127.0.0.1:8000/admin 管理数据
9 新建news/url.py文件编辑url路径，在views中添加函数，在templates中加入模板
10 访问http://127.0.0.1:8000/news/articles/2020 查询2020年的新闻

### 更改案例news为作业上交平台
在models中更改class，创建数据库Student Homework，设置数据格式
在admin中加入数据库
python manage.py makemigrations
在templates目录下创建HTML文件，内容为提交作业的界面格式
在views中创建class，将数据库models和HTML文件以及在页面中出现的选项关联起来
在url中添加path
