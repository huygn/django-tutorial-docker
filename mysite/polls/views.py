from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.db.models import F

from .models import Question, Choice


def index(request):
    latest_question_list = Question.objects.filter(
        pub_date__lte=timezone.now()
    ).order_by('-pub_date')[:5]
    context = dict(latest_question_list=latest_question_list)
    return render(request, 'polls/index.html', context=context)

def detail(request, question_id):
    question = get_object_or_404(
        Question,
        pk=question_id,
        pub_date__lte=timezone.now())
    context = dict(question=question)
    return render(request, 'polls/detail.html', context=context)

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = dict(question=question)
    return render(request, 'polls/results.html', context=context)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        # selected_choice.votes += 1
        # Use F() class to avoid race condition
        # https://docs.djangoproject.com/en/1.9/ref/models/expressions/#avoiding-race-conditions-using-f
        selected_choice.votes = F('votes') + 1
        selected_choice.save()
        # contruct results url using namespace
        results_url = reverse('polls:results', args=(question.id,))
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(results_url)
