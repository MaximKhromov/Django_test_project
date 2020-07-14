from django.shortcuts import render
from .models import Question, Answers
from django.http import Http404
from .forms import AnsForm


# Create your views here.
def index(request):
    try:
        questions = Question.objects.all() #получаем все объекты модели в виде списка question
    except Question.DoesNotExist:
        raise Http404("Question does not exist")

    try:
        questions_f = Question.objects.all().filter(question_name__contains='Илон') #получаем все объекты модели в виде списка question
    except Question.DoesNotExist:
        raise Http404("Question does not exist")

    answer = Answers.objects.all() #получаем все ответы

    form=AnsForm()
    context={
        'form': form
    }

    return render(request, 'test1/index.html', {'quest': questions, 'quest_f': questions_f, 'answ': answer}) #возвращает шаблон с переданными в него объектами модели

def about(request):
    return render(request, 'test1/about.html') #возвращает шаблон

