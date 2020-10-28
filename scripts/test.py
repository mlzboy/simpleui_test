from oj.models import *


# python manage.py runscript test
def run():
    print("="*10)
    t = Teacher.objects.get(no="2018000001")
    # print(t.course_set.all())#反向查询
    for c in Course.objects.all():
        print(c.name,c.teacher.name,c.class_set.all())

    print("="*10)
    for c in Class.objects.all():
        print(c.name,c.courses.all(),c.student_set.all())