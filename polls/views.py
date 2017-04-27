from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.urls import reverse
from django.db.models import F
from .models import Choice, Question

import code 
# code.interact(local=dict(globals(), **locals()))

def index(request):
  latest_question_list = Question.objects.order_by('-pub_date')[:5]
  context = {'latest_question_list': latest_question_list}
  return render(request, 'polls/index.html', context)

def new(request):
  return HttpResponse("Hello, world. You're at the new page.")

def detail(request, question_id):
  question = get_object_or_404(Question, pk=question_id)
  return render(request, 'polls/detail.html', {'question': question})

def vote(request, question_id):
  question = get_object_or_404(Question, pk=question_id)
  try: 
    selected_choice = question.choice_set.get(pk=request.POST['choice'])
  except (KeyError, Choice.DoesNotExist):
    context = {
      'question': question,
      'error_message': 'You didnt select a choice.'
    }
    return render(request, 'polls/detail.html', context)
  else:
    selected_choice.votes = F('votes') + 1
    selected_choice.save()
    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def results(request, question_id):
  question = get_object_or_404(Question, pk=question_id)
  return render(request, 'polls/results.html', {'question': question})
