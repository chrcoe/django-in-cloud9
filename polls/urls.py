from django.conf.urls import patterns, url

from polls import views

urlpatterns = patterns('',
    # the 'hard way'
    # # /polls/
    # url(r'^$', views.index, name='index'),
    # # /polls/5/
    # url(r'^(?P<question_id>\d+)/$', views.detail, name='detail'),
    # # /polls/5/results/
    # url(r'^(?P<question_id>\d+)/results/$', views.results, name='results'),
    # # /polls/5/vote/
    # url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
    
    # code reuse way:
    url(r'^$', views.IndexView.as_view(), name='index'), # /polls/
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'), # uses generic PK indicator
    url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'), # uses the specific question_id indicator

)