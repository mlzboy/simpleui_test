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
    if request.method == 'POST':
        data = request.POST.get('data', '')
        option = request.POST.getlist('option', '')
        print(option)
        print(data)
        r = exec_py_code.exec_main(data.replace('\n', ''))
        output = r.get('output', None)
    question = models.Question.objects.get(id=question_id)
    if str(question.category) == '编程题':
        return render(request, 'oj/bct_question_page.html',
                      {'question': question,
                       'data': data,
                       'output': output})
    else:
        return render(request, 'oj/xzt_question_page.html',
                      {'question': question,
                       'data': data,
                       'output': output})




