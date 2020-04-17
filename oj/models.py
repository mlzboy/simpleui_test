from django.db import models

class Course(models.Model):
    name = models.CharField(max_length = 40,null = True,blank = True,verbose_name='课程')
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE,verbose_name='授课教师')
    #一门课一定有一个老师上（多对一的一这一端），一个老师有多门课，c.teacher进行定位该课程的老师(链式表达：course.teacher.name,通过点属性进行链式的表达)
    # classs = models.ManyToManyField(Class)#多对多可以写在任意一个类(Class、Course)中，但是只能写一次，具体写在哪边，根据自己业务情况
    # course.class_set.all()
    # t.course_set()某个老师教授的所有课程
    class Meta:
        verbose_name = "课程管理"
        verbose_name_plural = "课程管理"

    def __str__(self):     
        return self.name


class Class(models.Model):
    name = models.CharField(max_length = 40,null = True,blank = True,verbose_name='班级名')
    courses = models.ManyToManyField(Course,verbose_name='所上课程')
    #建立多对多关系，一般不需要指定中间表，由ORM系统自动维护，通过c.courses.all()来表示该班的所有课程
    #设计课程和班级之间的多对多关系，不再建立课程与学生之间的多对多关系，
    # 虽然也可以，此举的目的是班级主体的层次粒度比学生主体要高，
    # 通过班级来建立课程和学生之间的桥梁，不再在课程和学生直接再建立多对多的关系，
    # 有力于理清关注，在增加课程或是增加班级亦或是增加学生时不再需要维护多边的关系，减少不必要的代码复杂度
    #c.student_set.all()
    class Meta:
        verbose_name = "班级管理"
        verbose_name_plural = "班级管理"

    def __str__(self):
        return self.name   


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length = 40,null = True,blank = True,verbose_name='姓名')
    no = models.CharField(max_length = 40,null = True,blank = True,verbose_name='学号')
    passwordd = models.CharField(max_length = 40,null = True,blank = True,verbose_name='密码')
    # 一对多外键设置，'多'的模型类设置外键，注意需要带参数on_delete
    #设置外键的方法中，第一个参数为外键对应的类名，一般加上引号。如果不加引号，那该类必须创建在主表前面
    classs = models.ForeignKey(Class, on_delete=None,verbose_name='所在班级')
    exams = models.ManyToManyField('Exam',through='StudentExamScore')
    class Meta:
        verbose_name = "学生管理"
        verbose_name_plural = "学生管理"

    def __str__(self):
        return self.name


 

class Teacher(models.Model):
    name = models.CharField(max_length = 40,null = True,blank = True,verbose_name='姓名')
    no = models.CharField(max_length = 40,null = True,blank = True,verbose_name='工号')
    passwordd = models.CharField(max_length = 40,null = True,blank = True,verbose_name='密码')
    #t.course_set.all()
    class Meta:
        verbose_name = "教师管理"
        verbose_name_plural = "教师管理"

    def __str__(self):
        return self.name





class Question(models.Model):
    question = models.CharField(max_length = 400,null = True,blank = True,verbose_name='课程')
    option1 = models.CharField(max_length = 400,null = True,blank = True,verbose_name='选项一')
    option2 = models.CharField(max_length = 400,null = True,blank = True,verbose_name='选项二')
    option3 = models.CharField(max_length = 400,null = True,blank = True,verbose_name='选项三')
    option4 = models.CharField(max_length = 400,null = True,blank = True,verbose_name='选项四')
    right_answer = models.CharField(max_length = 40,null = True,blank = True,verbose_name='正确答案')
    category = models.ForeignKey('Category', on_delete=None,verbose_name='题型')
    tags = models.ManyToManyField('Tag',verbose_name='知识点')

    class Meta:
        verbose_name = "题库管理"
        verbose_name_plural = "题库管理"

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length = 40,null = True,blank = True,verbose_name='题型分类')
    class Meta:
        verbose_name = "题型管理"
        verbose_name_plural = "题型管理"

class Tag(models.Model):
    name = models.CharField(max_length = 40,null = True,blank = True,verbose_name='知识点')
   
    class Meta:
        verbose_name = "知识点管理"
        verbose_name_plural = "知识点管理"

    def __str__(self):
        return self.name

class Exam(models.Model):
    name = models.CharField(max_length = 40,null = True,blank = True,verbose_name='考测名称')
    questions = models.ManyToManyField(Question,verbose_name='试题集')
    course = models.ForeignKey(Course,on_delete=models.CASCADE,verbose_name='考试对应的课程')
    class Meta:
        verbose_name = "考试管理"
        verbose_name_plural = "考试管理"

    def __str__(self):
        return self.name

class StudentExamScore(models.Model):
    score = models.DecimalField(max_digits=4,decimal_places=1,verbose_name='测验成绩')
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam,on_delete=models.CASCADE)
    

    class Meta:
        verbose_name = "测验分数管理"
        verbose_name_plural = "测验分数管理"

    def __str__(self):
        return self.name

class Answer(models.Model):
    answer = models.CharField(max_length = 40,null = True,blank = True,verbose_name='测验名称')
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    student_exam_score = models.ForeignKey(StudentExamScore,on_delete=models.CASCADE)
    class Meta:
        verbose_name = "学生答案管理"
        verbose_name_plural = "学生答案管理"

    def __str__(self):
        return self.name
