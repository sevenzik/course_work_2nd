from django.db import models

# Create your models here.


class Task(models.Model):
    THEMES = (
        ('Гамильтонов цикл', 'Гамильтонов цикл'),
        ('Эйлеров цикл', 'Эйлеров цикл'),
    )
    theme = models.CharField(max_length=50, choices=THEMES)
    num = models.BigIntegerField(default=0)
    question = models.TextField()
    graph = models.TextField()
    answer = models.CharField(max_length=20, default="")

    def __str__(self):
        return self.theme + " " + str(self.num)


class DoneTest(models.Model):
    login = models.CharField(max_length=50, default="")
    numberOfQuestions = models.BigIntegerField(default=0)
    numberOfRightAnswers = models.BigIntegerField(default=0)
    date_started = models.DateTimeField(editable=True)

    theme1 = models.CharField(max_length=50, default="")
    num1 = models.BigIntegerField(default=0)
    user_ans1 = models.CharField(max_length=20, default="")
    is_right1 = models.BooleanField(default=True)

    theme2 = models.CharField(max_length=50, default="")
    num2 = models.BigIntegerField(default=0)
    user_ans2 = models.CharField(max_length=20, default="")
    is_right2 = models.BooleanField(default=True)

    theme3 = models.CharField(max_length=50, default="")
    num3 = models.BigIntegerField(default=0)
    user_ans3 = models.CharField(max_length=20, default="")
    is_right3 = models.BooleanField(default=True)

    theme4 = models.CharField(max_length=50, default="")
    num4 = models.BigIntegerField(default=0)
    user_ans4 = models.CharField(max_length=20, default="")
    is_right4 = models.BooleanField(default=True)

    theme5 = models.CharField(max_length=50, default="")
    num5 = models.BigIntegerField(default=0)
    user_ans5 = models.CharField(max_length=20, default="")
    is_right5 = models.BooleanField(default=True)

    theme6 = models.CharField(max_length=50, default="")
    num6 = models.BigIntegerField(default=0)
    user_ans6 = models.CharField(max_length=20, default="")
    is_right6 = models.BooleanField(default=True)

    theme7 = models.CharField(max_length=50, default="")
    num7 = models.BigIntegerField(default=0)
    user_ans7 = models.CharField(max_length=20, default="")
    is_right7 = models.BooleanField(default=True)

    theme8 = models.CharField(max_length=50, default="")
    num8 = models.BigIntegerField(default=0)
    user_ans8 = models.CharField(max_length=20, default="")
    is_right8 = models.BooleanField(default=True)

    theme9 = models.CharField(max_length=50, default="")
    num9 = models.BigIntegerField(default=0)
    user_ans9 = models.CharField(max_length=20, default="")
    is_right9 = models.BooleanField(default=True)

    theme10 = models.CharField(max_length=50, default="")
    num10 = models.BigIntegerField(default=0)
    user_ans10 = models.CharField(max_length=20, default="")
    is_right10 = models.BooleanField(default=True)

    theme11 = models.CharField(max_length=50, default="")
    num11 = models.BigIntegerField(default=0)
    user_ans11 = models.CharField(max_length=20, default="")
    is_right11 = models.BooleanField(default=True)

    theme12 = models.CharField(max_length=50, default="")
    num12 = models.BigIntegerField(default=0)
    user_ans12 = models.CharField(max_length=20, default="")
    is_right12 = models.BooleanField(default=True)

    theme13 = models.CharField(max_length=50, default="")
    num13 = models.BigIntegerField(default=0)
    user_ans13 = models.CharField(max_length=20, default="")
    is_right13 = models.BooleanField(default=True)

    theme14 = models.CharField(max_length=50, default="")
    num14 = models.BigIntegerField(default=0)
    user_ans14 = models.CharField(max_length=20, default="")
    is_right14 = models.BooleanField(default=True)

    theme15 = models.CharField(max_length=50, default="")
    num15 = models.BigIntegerField(default=0)
    user_ans15 = models.CharField(max_length=20, default="")
    is_right15 = models.BooleanField(default=True)

    theme16 = models.CharField(max_length=50, default="")
    num16 = models.BigIntegerField(default=0)
    user_ans16 = models.CharField(max_length=20, default="")
    is_right16 = models.BooleanField(default=True)

    theme17 = models.CharField(max_length=50, default="")
    num17 = models.BigIntegerField(default=0)
    user_ans17 = models.CharField(max_length=20, default="")
    is_right17 = models.BooleanField(default=True)

    theme18 = models.CharField(max_length=50, default="")
    num18 = models.BigIntegerField(default=0)
    user_ans18 = models.CharField(max_length=20, default="")
    is_right18 = models.BooleanField(default=True)

    theme19 = models.CharField(max_length=50, default="")
    num19 = models.BigIntegerField(default=0)
    user_ans19 = models.CharField(max_length=20, default="")
    is_right19 = models.BooleanField(default=True)

    theme20 = models.CharField(max_length=50, default="")
    num20 = models.BigIntegerField(default=0)
    user_ans20 = models.CharField(max_length=20, default="")
    is_right20 = models.BooleanField(default=True)
