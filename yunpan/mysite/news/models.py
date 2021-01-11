from django.db import models

class Student(models.Model):#学生基本信息
    full_name = models.CharField(max_length=70)
    #age = models.IntegerField()
    class Sex(models.IntegerChoices):#性别 下拉菜单选择
        MALE = 1,'男'
        FEMALE = 2,'女'
        other = 3,'其他'
    sex = models.IntegerField(choices=Sex.choices)
    def __str__(self):
        return self.full_name

class Homework(models.Model):#提交内容
    commit_date = models.DateField(auto_now = True)#自动设置时间
    headline = models.CharField(max_length=200)#标题，200字以内
    attach = models.FileField()#上传文件
    remark = models.TextField()#上传文字内容
    student = models.ForeignKey(Student, on_delete=models.CASCADE)#提交人，引用外键student

    def __str__(self):
        return self.headline
# Create your models here.
