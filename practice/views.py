from django.shortcuts import render
from practice.models import Task
from django.views.generic import TemplateView
import random

# Create your views here.

class TestIsOnView(TemplateView):
    template_name = 'practice/test_is_on.html'

    def get(self, request):



def gamiltontest(request):
    return render(request, 'practice/gamilton_test.html')


def gamiltontestison(request):
    # task_theme = request.session.get('task_theme', 'Гамильтонов цикл')
    # task_num = request.session.get('task_num', 0)
    # data = {"question1": {'question': Task.objects.get(num=0).question, 'num': 1},
    #         "question2": {'question': Task.objects.get(num=1).question, 'num': 2}}
    #
    # data = {'data': Task.objects.all()}
    # data = {'d': int(len(Task.objects.all()))}
    # request.session['task_num'] = 1

    gam_questions = Task.objects.filter(theme='Гамильтонов цикл')
    our_questions = random.sample(list(gam_questions), 2)
    our_data = list()
    for i in range(len(our_questions)):
        our_data.append([i + 1, our_questions[i]])

    data = {'data': our_data}
    return render(request, 'practice/test_is_on.html', context=data)


def gamiltontestfinished(request):
    return render(request, 'practice/test_finished.html')
