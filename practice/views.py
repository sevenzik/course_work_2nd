from django.shortcuts import render
from django.views.generic import TemplateView
from practice.models import Task, DoneTest
from practice.forms import TestForm
import random
import datetime

# Create your views here.


class TestIsOnView(TemplateView):
    template_name_get = 'practice/test_is_on.html'
    template_name_post = 'practice/test_finished.html'
    template_not_logged = 'registration/login.html'

    def get(self, request):
        number_of_questions = 2
        if request.user.is_authenticated:
            gam_questions = Task.objects.filter(theme='Гамильтонов цикл')
            our_questions = random.sample(list(gam_questions), number_of_questions)
            our_data = list()
            for i in range(len(our_questions)):
                our_data.append([i + 1, our_questions[i]])

            now = datetime.datetime.now()
            data = {'data': our_data, 'time': str(now)}

            newDoneTest = DoneTest(date_started=now, login=request.user.username, numberOfQuestions=len(our_questions))
            newDoneTest.save()

            for i in range(1, number_of_questions + 1):
                values_for_update = {'theme'+str(i): our_questions[i - 1].theme, 'num' + str(i): our_questions[i - 1].num}
                DoneTest.objects.filter(login=request.user.username).\
                    update_or_create(date_started=now, defaults=values_for_update)

            return render(request, self.template_name_get, context=data)
        else:
            return render(request, self.template_not_logged)

    def post(self, request):
        ans = list()
        number_of_questions = request.POST['count']

        for i in range(1, int(number_of_questions) + 1):
            ans.append(request.POST['answer' + str(i)])

        donetest = DoneTest.objects.get(date_started=request.POST['time'], login=request.user.username)

        for i in range(1, int(number_of_questions) + 1):
            # values_for_update = {'user_ans' + str(i): request.POST['answer' + str(i)],
            #                      'is_right' + str(i): request.POST['answer' + str(i)] ==
            #                                           Task.objects.get(theme=donetest['theme' + str(i)],
            #                                                            num=donetest['num' + str(i)]).answer}
            # DoneTest.objects.filter(login=request.user.username).update_or_create(date_started=request.POST['time'],
            #                                                                       defaults=values_for_update)

            rightness = str(str(request.POST['answer' + str(i)])
                    == str(Task.objects.get(theme=getattr(donetest, 'theme' + str(i)), num=getattr(donetest, 'num' + str(i))).answer))

            setattr(donetest, 'user_ans' + str(i), request.POST['answer' + str(i)])
            setattr(donetest, 'is_right' + str(i), rightness)

        args = {'ans': ans, 'count': number_of_questions}
        donetest.save()

        return render(request, self.template_name_post, args)


def gamiltontest(request):
    return render(request, 'practice/gamilton_test.html')


def gamiltontestfinished(request):
    return render(request, 'practice/test_finished.html')
