from django.db import models

# Create your models here.
from django.db import models


class Student(models.Model):
    student_number = models.CharField(max_length=128, unique=True, verbose_name='学号')
    password = models.CharField(max_length=256, verbose_name='密码')

    def __str__(self):
        return self.student_number

    class Meta:
        verbose_name = '学生'
        verbose_name_plural = '学生'
