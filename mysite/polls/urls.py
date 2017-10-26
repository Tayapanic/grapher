from django.conf.urls import url

from . import views
app_name='polls'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^graph_type/$',views.graph_type,name='graph_type'),
    url(r'^piechart_input/$',views.piechart_input,name='piechart_input'),
    url(r'^graph_input/$',views.graph,name='graph_input'),
    url(r'^histogram/$',views.histogram,name='histogram'),
    url(r'^y_as_x/$',views.y_as_x,name='y_as_x'),
    url(r'^z_as_yx/$',views.z_as_yx,name='z_as_yx'),
    url(r'^polar_plot/$',views.polar_plot,name='polar_plot'),

]