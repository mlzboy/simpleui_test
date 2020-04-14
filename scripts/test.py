from oj.models import *

def run():
    t = Teacher.objects.get(no="2018000001")
    print(t.course_set.all())#反向查询
    for c in Course.objects.all():
        print(c.name,c.teacher.name,c.class_set.all())

    print("="*10)
    for c in Class.objects.all():
        print(c.name,c.courses.all())