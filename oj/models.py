from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length = 40,null = True,blank = True,verbose_name='姓名')
    no = models.IntegerField(null = True,blank = True,verbose_name='学号')
    password = models.CharField(max_length = 40,null = True,blank = True,verbose_name='密码')

    class Meta:
        verbose_name = "学生管理"
        verbose_name_plural = "学生管理"

    def __str__(self):
        return self.name


class Class(models.Model):
    name = models.CharField(max_length = 400,null = True,blank = True,verbose_name='班级名')
    class Meta:
        verbose_name = "班级管理"
        verbose_name_plural = "班级管理"

    def __str__(self):
        return self.name    

class Teacher(models.Model):
    name = models.CharField(max_length = 400,null = True,blank = True,verbose_name='姓名')
    class Meta:
        verbose_name = "教师管理"
        verbose_name_plural = "教师管理"

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length = 400,null = True,blank = True,verbose_name='课程')
    class Meta:
        verbose_name = "课程管理"
        verbose_name_plural = "课程管理"

    def __str__(self):
        return self.name


class Question(models.Model):
    question = models.CharField(max_length = 400,null = True,blank = True,verbose_name='课程')
    option1 = models.CharField(max_length = 400,null = True,blank = True,verbose_name='选项一')
    option2 = models.CharField(max_length = 400,null = True,blank = True,verbose_name='选项二')
    option3 = models.CharField(max_length = 400,null = True,blank = True,verbose_name='选项三')
    option4 = models.CharField(max_length = 400,null = True,blank = True,verbose_name='选项四')
    answer = models.CharField(max_length = 400,null = True,blank = True,verbose_name='选项四')
    category = models.CharField(max_length = 400,null = True,blank = True,verbose_name='类型')
    
    class Meta:
        verbose_name = "题库管理"
        verbose_name_plural = "题库管理"

    def __str__(self):
        return self.name



class Exam(models.Model):
    name = models.CharField(max_length = 400,null = True,blank = True,verbose_name='测验名称')
    
    class Meta:
        verbose_name = "测验管理"
        verbose_name_plural = "测验管理"

    def __str__(self):
        return self.name


class Exam(models.Model):
    score = models.IntegerField(null = True,blank = True,verbose_name='测验成绩')
    
    class Meta:
        verbose_name = "测验管理"
        verbose_name_plural = "测验管理"

    def __str__(self):
        return self.name

class Answer(models.Model):
    answer = models.CharField(max_length = 400,null = True,blank = True,verbose_name='测验名称')
    
    class Meta:
        verbose_name = "测验管理"
        verbose_name_plural = "测验管理"

    def __str__(self):
        return self.name
