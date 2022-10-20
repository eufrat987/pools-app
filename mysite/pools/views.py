from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Question


# Create your views here.

def index(request):
    latest_questions = Question.objects.order_by('-pub_date')[:5]
    return render(request, 'pools/index.html', {'latest_questions': latest_questions})


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'pools/detail.html', {'question': question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'pools/results.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        sel = question.choices_set.get(pk=request.POST['choice'])
    except:
        return render(request, 'pools/detail.html', {'question': question,
                                                     'error_message': 'Choose!'})
    else:
        sel.votes += 1
        sel.save()
        return HttpResponseRedirect(reverse('pools:results', args=(question_id,)))
