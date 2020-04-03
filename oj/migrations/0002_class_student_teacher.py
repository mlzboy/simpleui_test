# Generated by Django 2.1.7 on 2020-03-21 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('oj', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=400, null=True, verbose_name='班级名')),
            ],
            options={
                'verbose_name': '班级管理',
                'verbose_name_plural': '班级管理',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=400, null=True, verbose_name='姓名')),
                ('no', models.IntegerField(blank=True, null=True, verbose_name='学号')),
                ('password', models.CharField(blank=True, max_length=400, null=True, verbose_name='密码')),
            ],
            options={
                'verbose_name': '学生管理',
                'verbose_name_plural': '学生管理',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=400, null=True, verbose_name='姓名')),
            ],
            options={
                'verbose_name': '教师管理',
                'verbose_name_plural': '教师管理',
            },
        ),
    ]
