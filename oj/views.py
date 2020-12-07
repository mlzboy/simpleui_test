from django.shortcuts import render, HttpResponseRedirect, redirect
from oj import models
from . import exec_py_code
from django.core.paginator import Paginator
from django.urls import reverse


def question_all(request):
    questions = models.Question.objects.all()
    default1 = ''
    difficulty = request.GET.get('d', None)
    id = request.GET.get('id', None)
    question = None
    if id:
        for qu in questions:
            if str(qu.id) == str(id):
                question = qu
                default1 = question.functionname
                break
    current_pagnum = request.GET.get('page', 1)
    paginator = Paginator(questions, 20)
    page_list = paginator.page(number=current_pagnum)
    if difficulty:
        # print(difficulty)
        dq = []
        for question in questions:
            if question.difficulty == difficulty:
                dq.append(question)
        return render(request, 'oj/codeeditor.html', locals())
    # 处理提交的代码
    submit_action = request.GET.get('submit_action', None)
    if submit_action:
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
            if sl1:
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
            if sl2:
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
            if sl3:
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
            if sl4:
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
    return render(request, 'oj/codeeditor.html', locals())


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
    questions = models.Question.objects.all()
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
            if sl1:
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
            if sl2:
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
            if sl3:
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
            if sl4:
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
            current_pagnum = request.GET.get('page', 1)
            id = request.GET.get('id')
            return HttpResponseRedirect('/questions/all/?page={}&id={}'.format(current_pagnum, id))
            # return render(request, 'oj/codeeditor.html', locals())
            # return redirect('question_all')

        # else:  # 选择题的情况
        #     option = request.POST.getlist('option', '')
        #     print(option)
        #     return render(request, 'oj/xzt_question_page.html',
        #                   {'question': question,
        #                    'data': data,
        #                    'code_output': code_output,
        #                    'tags': tags})








