# Homework2.0
 分布式系统和云计算
## 1创建云盘文件夹

## 案例news
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

## 更改案例news为作业上交平台
在models中更改class