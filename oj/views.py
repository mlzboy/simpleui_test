from django.shortcuts import render
from oj import models
from . import exec_py_code

def question_all(request):
    questions = models.Question.objects.all()
    return render(request, 'oj/question_all.html',
                  {'questions': questions})


def question_page(request, question_id):
    question = models.Question.objects.get(id=question_id)
    if str(question.category) == '编程题':
        return render(request, 'oj/bct_question_page.html',
                      {'question': question})
    else:
        return render(request, 'oj/xzt_question_page.html',
                      {'question': question})


def submit_action(request, question_id):
    question = models.Question.objects.get(id=question_id)
    if request.method == 'POST':
        # 实例的四个输出
        sl1_output = ''
        sl2_output = ''
        sl3_output = ''
        sl4_output = ''
        # 提交的代码
        data = request.POST.get('data', '')
        print(data)
        r = exec_py_code.exec_main(data.replace('\n', ''))
        code_output = r.get('output', None)
        if str(question.category) == '编程题':
            sl1 = question.example1
            sl1 = '\nprint({})'.format(sl1)
            sl2 = question.example2
            sl2 = '\nprint({})'.format(sl2)
            sl3 = question.example3
            sl3 = '\nprint({})'.format(sl3)
            sl4 = question.example4
            sl4 = '\nprint({})'.format(sl4)
            data2 = data
            sl = sl1+sl2+sl3+sl4
            data2 += sl
            # 实例答案的返回
            sl_res = exec_py_code.exec_main(data2)
            if sl_res["code"] == 'Success':
                sl_output = sl_res.get('output', None)
                sl_output = sl_output.split('\n')[:-1]
                # print(sl_output)
                if len(sl_output) > 4:
                    sl_output = sl_output[-4:]
                    # print(sl_output)
                    sl1_output = sl_output[0]
                    sl2_output = sl_output[1]
                    sl3_output = sl_output[2]
                    sl4_output = sl_output[3]
                elif len(sl_output) == 4:
                    sl1_output = sl_output[0]
                    sl2_output = sl_output[1]
                    sl3_output = sl_output[2]
                    sl4_output = sl_output[3]
            else:
                sl_output = sl_res.get('output', None)
                sl1_output = sl_output
                # print(sl_output)
        else:  # 选择题的情况
            option = request.POST.getlist('option', '')
            print(option)

    if str(question.category) == '编程题':
        return render(request, 'oj/bct_question_page.html',
                      {'question': question,
                       'data': data,
                       'code_output': code_output,
                       'sl1_output': sl1_output,
                       'sl2_output': sl2_output,
                       'sl3_output': sl3_output,
                       'sl4_output': sl4_output,
                       })
    else:
        return render(request, 'oj/xzt_question_page.html',
                      {'question': question,
                       'data': data,
                       'code_output': code_output})




