#!/usr/bin/env python3
#encoding=utf-8
from oj.models import *

def run():
    t = Teacher(name = "毛老师",no="2018000001",passwordd="123456")
    t.save()
    c1 = Course(name = "Python数据分析",teacher = t)
    c1.save()
    cls = Class(name="商数181")
    cls.save()
    cls.courses.add(c1)
    # cls.save()
    c2 = Course(name= "数据采集与处理", teacher = t)
    c2.save()
    cls2 = Class(name="商数191")
    cls2.save()
    cls2.courses.add(c2)
    # cls2.save()
    cls3 = Class(name="商数192")
    cls3.save()
    cls3.courses.add(c2)
    # cls3.save()
    #加入自身今年的课程，学生
    s1 = Student(name="楼倩波",no="201800004",passwordd="1111111",classs = cls)
    s1.save()
    s2 = Student(name="高敬",no="201800005",passwordd="1111111",classs = cls)
    s2.save()



