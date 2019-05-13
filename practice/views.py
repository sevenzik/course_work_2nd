from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from practice.models import Task, DoneTest
from django.contrib.auth.models import User
from userprofile.models import UserProfile
import random
import datetime

# Create your views here.


class TestIsOnView(TemplateView):
    template_name_get = 'practice/test_is_on.html'
    template_name_post = 'practice/test_finished.html'
    template_not_logged = 'registration/login.html'

    def get(self, request):
        u = User.objects.get(username=request.user.username)
        number_of_questions = u.userprofile.lastNumberOfQuestions
        filt_theme = u.userprofile.last_theme
        if request.user.is_authenticated:
            if filt_theme != "all":
                gam_questions = Task.objects.filter(theme=filt_theme)
            else:
                gam_questions = Task.objects.all()
            our_questions = random.sample(list(gam_questions), number_of_questions)
            our_data = list()
            for i in range(len(our_questions)):
                our_data.append([i + 1, our_questions[i]])

            now = datetime.datetime.now()
            data = {'data': our_data, 'time': str(now), 'count': number_of_questions}

            newDoneTest = DoneTest(date_started=now, login=request.user.username, numberOfQuestions=number_of_questions)
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
        right = 0
        for i in range(1, int(number_of_questions) + 1):

            rightness = str(str(request.POST['answer' + str(i)])
                    == str(Task.objects.get(theme=getattr(donetest, 'theme' + str(i)), num=getattr(donetest, 'num' + str(i))).answer))
            if rightness == "True":
                right += 1
            setattr(donetest, 'user_ans' + str(i), request.POST['answer' + str(i)])
            setattr(donetest, 'is_right' + str(i), rightness)

        args = {'ans': ans, 'count': number_of_questions, 'right': right}
        donetest.numberOfRightAnswers = right
        donetest.save()

        u = UserProfile.objects.get(user=request.user)
        setattr(u, 'test_started', 0)

        u.save()

        return render(request, self.template_name_post, args)


def gamiltontest(request):
    if request.method == 'GET':
        return render(request, 'practice/gamilton_test.html')
    elif request.method == 'POST':
        if request.user.is_authenticated:
            u, created = UserProfile.objects.get_or_create(user=request.user)
            # setattr(u, 'lastNumberOfQuestions',
            #         2
            #        # request.POST['num_of_questions']
            #         )

            u.lastNumberOfQuestions = request.POST['num_of_questions']
            u.last_theme = "Гамильтонов цикл"
            setattr(u, 'test_started', "True")
            u.save()
            return redirect('/practice/gamilton/test/')
        else:
            return redirect('/sign/login/')


def eulertest(request):
    if request.method == 'GET':
        return render(request, 'practice/euler_test.html')
    elif request.method == 'POST':
        if request.user.is_authenticated:
            u, created = UserProfile.objects.get_or_create(user=request.user)
            # setattr(u, 'lastNumberOfQuestions',
            #         2
            #        # request.POST['num_of_questions']
            #         )

            u.lastNumberOfQuestions = request.POST['num_of_questions']
            u.last_theme = "Эйлеров цикл"
            setattr(u, 'test_started', "True")
            u.save()
            return redirect('/practice/gamilton/test/')
        else:
            return redirect('/sign/login/')


def alltest(request):
    if request.method == 'GET':
        return render(request, 'practice/all_test.html')
    elif request.method == 'POST':
        if request.user.is_authenticated:
            u, created = UserProfile.objects.get_or_create(user=request.user)
            u.lastNumberOfQuestions = request.POST['num_of_questions']
            u.last_theme = "all"
            setattr(u, 'test_started', "True")
            u.save()
            return redirect('/practice/gamilton/test/')
        else:
            return redirect('/sign/login/')


def yourtestlist(request):
    if request.user.is_authenticated:
        donetests = DoneTest.objects.filter(login=request.user.username).order_by('date_started')
        donetests = donetests.reverse()
        data = {'data': donetests}
        return render(request, 'practice/yourtestlist.html', context=data)
    else:
        return redirect('/sign/login/')


def yourtest(request, id):
    if DoneTest.objects.filter(id=id).count() == 0:
        return render(request, 'mainApp/no_permission.html')

    donetest = DoneTest.objects.get(id=id)

    if not request.user.is_authenticated:
        return redirect('/sign/login/')
    elif request.user.username != donetest.login:
        return render(request, 'mainApp/no_permission.html')

    our_questions = []

    for i in range(1, 1 + donetest.numberOfQuestions):
        our_questions.append([i, Task.objects.get(theme=getattr(donetest, 'theme' + str(i)), num=getattr(donetest, 'num' + str(i))),
                                 getattr(donetest, 'user_ans' + str(i)), getattr(donetest, 'is_right' + str(i))])

    data = {'questions': our_questions, 'time': str(getattr(donetest, 'date_started')), 'count': getattr(donetest, 'numberOfQuestions')}

    return render(request, 'practice/yourtest.html', context=data)



