from django.shortcuts import render
from oj import models
from . import exec_py_code
import re


def question_all(request):
    questions = models.Question.objects.all()
    return render(request, 'oj/question_all.html',
                  {'questions': questions})


def question_page(request, question_id):
    question = models.Question.objects.get(id=question_id)
    tags = question.tags.all()
    if str(question.category) == '编程题':
        default1 = question.functionname
        return render(request, 'oj/bct_question_page.html',
                      {'question': question,
                       'default1': default1,
                       'tags': tags,})
    else:
        return render(request, 'oj/xzt_question_page.html',
                      {'question': question,
                       'tags': tags,})


def submit_action(request, question_id):
    question = models.Question.objects.get(id=question_id)
    tags = question.tags.all()
    if request.method == 'POST':
        # 实例的四个输出
        sl1_output = ''
        sl2_output = ''
        sl3_output = ''
        sl4_output = ''
        # 提交的代码
        data = request.POST.get('data', '')
        # print('data',data)
        r = exec_py_code.exec_main(data.replace('\n', ''))
        code_output = r.get('output', None)
        if str(question.category) == '编程题':
            data2 = data
            sl1 = question.example1
            sl1 = '\nprint({})'.format(sl1)
            if data2:
                data3 = data2 + sl1
                sl_res = exec_py_code.exec_main(data3)
                if sl_res["code"] == 'Success':
                    sl_output = sl_res.get('output', None)
                    sl1_output = sl_output.split('\n')[-2].strip()
                else:
                    sl_output = sl_res.get('output', None)
                    sl1_output = sl_output
                    # print(sl_output)
            sl2 = question.example2
            sl2 = '\nprint({})'.format(sl2)
            if data2:
                data3 = data2 + sl2
                sl_res = exec_py_code.exec_main(data3)
                if sl_res["code"] == 'Success':
                    sl_output = sl_res.get('output', None)
                    sl2_output = sl_output.split('\n')[-2].strip()
                else:
                    sl_output = sl_res.get('output', None)
                    sl2_output = sl_output
                    # print(sl_output)
            sl3 = question.example3
            sl3 = '\nprint({})'.format(sl3)
            if data2:
                data3 = data2 + sl3
                sl_res = exec_py_code.exec_main(data3)
                if sl_res["code"] == 'Success':
                    sl_output = sl_res.get('output', None)
                    sl3_output = sl_output.split('\n')[-2].strip()
                else:
                    sl_output = sl_res.get('output', None)
                    sl3_output = sl_output
                    # print(sl_output)
            sl4 = question.example4
            sl4 = '\nprint({})'.format(sl4)
            if data2:
                data3 = data2 + sl4
                sl_res = exec_py_code.exec_main(data3)
                if sl_res["code"] == 'Success':
                    sl_output = sl_res.get('output', None)
                    sl4_output = sl_output.split('\n')[-2].strip()
                else:
                    sl_output = sl_res.get('output', None)
                    sl4_output = sl_output
                    # print(sl_output)
            default1 = question.functionname
            return render(request, 'oj/bct_question_page.html',
                          {'question': question,
                           'data': data,
                           'code_output': code_output,
                           'sl1_output': sl1_output,
                           'sl2_output': sl2_output,
                           'sl3_output': sl3_output,
                           'sl4_output': sl4_output,
                           'default1': default1,
                           'tags': tags
                           })
        else:  # 选择题的情况
            option = request.POST.getlist('option', '')
            print(option)
            return render(request, 'oj/xzt_question_page.html',
                          {'question': question,
                           'data': data,
                           'code_output': code_output,
                           'tags': tags})






