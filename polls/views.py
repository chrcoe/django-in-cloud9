from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.template import RequestContext, loader
from polls.models import Choice, Question
from django.core.urlresolvers import reverse
from django.views import generic

# Create your views here.
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     # template = loader.get_template('polls/index.html')
#     # context = RequestContext(request, {
#     #     'latest_question_list': latest_question_list,
#     # })
#     # # output = ', '.join([p.question_text for p in latest_question_list])
#     # return HttpResponse(template.render(context))
    
#     # shortcut
#     context = {'latest_question_list' : latest_question_list}
#     return render(request, 'polls/index.html', context)

# def detail(request, question_id):
#     # try:
#     #     question = Question.objects.get(pk=question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404
    
#     # context = {'question' : question}
#     # return render(request, 'polls/detail.html', context)
    
#     # shortcut
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question' : question})

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question':question})

# use Django's generic views:
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    
    def get_queryset(self):
        '''Return the last five published questions.'''
        return Question.objects.order_by('-pub_date')[:5] # most recent five polls based on pub_date
        
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    
class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'
    

def vote(request, question_id):
    # does not currently do anything with the vote, just responds with the text
    # need to build a template to handle this and reference here
    # return HttpResponse("You're voting on question %s." % question_id)
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))