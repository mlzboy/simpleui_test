# Generated by Django 2.1.7 on 2020-04-14 04:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(blank=True, max_length=40, null=True, verbose_name='测验名称')),
            ],
            options={
                'verbose_name': '学生答案管理',
                'verbose_name_plural': '学生答案管理',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=40, null=True, verbose_name='题型分类')),
            ],
            options={
                'verbose_name': '题型管理',
                'verbose_name_plural': '题型管理',
            },
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=40, null=True, verbose_name='班级名')),
            ],
            options={
                'verbose_name': '班级管理',
                'verbose_name_plural': '班级管理',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=40, null=True, verbose_name='课程')),
            ],
            options={
                'verbose_name': '课程管理',
                'verbose_name_plural': '课程管理',
            },
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=40, null=True, verbose_name='考测名称')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oj.Course')),
            ],
            options={
                'verbose_name': '考试管理',
                'verbose_name_plural': '考试管理',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(blank=True, max_length=400, null=True, verbose_name='课程')),
                ('option1', models.CharField(blank=True, max_length=400, null=True, verbose_name='选项一')),
                ('option2', models.CharField(blank=True, max_length=400, null=True, verbose_name='选项二')),
                ('option3', models.CharField(blank=True, max_length=400, null=True, verbose_name='选项三')),
                ('option4', models.CharField(blank=True, max_length=400, null=True, verbose_name='选项四')),
                ('right_answer', models.CharField(blank=True, max_length=40, null=True, verbose_name='正确答案')),
                ('category', models.ForeignKey(on_delete=None, to='oj.Category', verbose_name='题型')),
            ],
            options={
                'verbose_name': '题库管理',
                'verbose_name_plural': '题库管理',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=40, null=True, verbose_name='姓名')),
                ('no', models.CharField(blank=True, max_length=40, null=True, verbose_name='学号')),
                ('passwordd', models.CharField(blank=True, max_length=40, null=True, verbose_name='密码')),
                ('classs', models.ForeignKey(on_delete=None, to='oj.Class')),
            ],
            options={
                'verbose_name': '学生管理',
                'verbose_name_plural': '学生管理',
            },
        ),
        migrations.CreateModel(
            name='StudentExamScore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.DecimalField(decimal_places=1, max_digits=4, verbose_name='测验成绩')),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oj.Exam')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oj.Student')),
            ],
            options={
                'verbose_name': '测验分数管理',
                'verbose_name_plural': '测验分数管理',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=40, null=True, verbose_name='知识点')),
            ],
            options={
                'verbose_name': '知识点管理',
                'verbose_name_plural': '知识点管理',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=40, null=True, verbose_name='姓名')),
                ('no', models.CharField(blank=True, max_length=40, null=True, verbose_name='工号')),
                ('passwordd', models.CharField(blank=True, max_length=40, null=True, verbose_name='密码')),
            ],
            options={
                'verbose_name': '教师管理',
                'verbose_name_plural': '教师管理',
            },
        ),
        migrations.AddField(
            model_name='student',
            name='exams',
            field=models.ManyToManyField(through='oj.StudentExamScore', to='oj.Exam'),
        ),
        migrations.AddField(
            model_name='question',
            name='tags',
            field=models.ManyToManyField(to='oj.Tag', verbose_name='知识点'),
        ),
        migrations.AddField(
            model_name='exam',
            name='questions',
            field=models.ManyToManyField(to='oj.Question'),
        ),
        migrations.AddField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oj.Teacher'),
        ),
        migrations.AddField(
            model_name='class',
            name='courses',
            field=models.ManyToManyField(to='oj.Course'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oj.Question'),
        ),
        migrations.AddField(
            model_name='answer',
            name='student_exam_score',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oj.StudentExamScore'),
        ),
    ]
