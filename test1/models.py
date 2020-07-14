from django.db import models

# Create your models here.
# Каждый класс отвечает за свою табличку

class Question(models.Model):
    question_name = models.CharField('Наименование вопроса', max_length=50)
    question_text = models.TextField('Вопрос')  # поле вопроса в таблице
    question_answ1 = models.CharField('Вариант1', max_length=50)
    question_answ2 = models.CharField('Вариант2', max_length=50)
    question_answ3 = models.CharField('Вариант3', max_length=50)
    question_answ4 = models.CharField('Вариант4', max_length=50)
    pub_date = models.DateTimeField('date published') # поле даты в таблице

    # вызывается в момент попытки вывести на экран объект класса
    def __str__(self):
        return self.question_name

class Answers(models.Model):
    answ=models.CharField('Ответ', max_length=50)

#class Choise(models.Model):
    #question = models.ForeignKey(Question, on_delese=models.CASCADE)
    #choice_text = models.CharField(max_length=200)
    #votes = models.IntegerField(default=0)