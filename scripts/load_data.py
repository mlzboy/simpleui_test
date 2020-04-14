#!/usr/bin/env python3
#encoding=utf-8
from oj.models import *

def run():
    t = Teacher(name = "毛老师",no="2018000001",passwordd="123456")
    t.save()
    c = Course(name = "Python数据分析",teacher = t)
    c.save()
    cls = Class(name="商数181")
    cls.save()
    cls.courses.add(c)
    c.save()
    c2 = Course(name= "数据采集与处理", teacher = t)
    c2.save()
    cls2 = Class(name="商数191")
    cls2.save()
    cls2.courses.add(c2)
    cls2.save()
    cls3 = Class(name="商数192")
    cls3.save()
    cls3.courses.add(c2)
    cls3.save()


