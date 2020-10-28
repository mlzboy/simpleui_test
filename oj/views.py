from django.shortcuts import render
from oj import models


def question_all(request):
    questions = models.Question.objects.all()
    return render(request, 'oj/question_all.html',
                  {'questions': questions})


def question_page(request, question_id):
    question = models.Question.objects.get(id=question_id)
    return render(request, 'oj/question_page.html',
                  {'question': question})


def submit_action(request, question_id):
    if request.method == 'POST':
        data = request.POST.get('data', '')
        print(data)
        a = exec(data)
        print(a)
    question = models.Question.objects.get(id=question_id)
    return render(request, 'oj/question_page.html',
                  {'question': question,
                   'data': data})



