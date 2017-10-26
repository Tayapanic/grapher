from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .models import Question,Choice
from django.template import loader
from django.urls import reverse
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt,mpld3
from polls.graph_py.histogram import *
from polls.graph_py.y_as_x import *
from polls.graph_py.z_as_yx import *
from polls.graph_py.polar import *

from django.core.files.storage import FileSystemStorage
import json

def graph_type(request):
	return render(request,'polls/graph_type.html')

def polar_plot(request):
	if request.method=="POST":
		polar_function=request.POST['polar_function']
		polar_lower_limit=request.POST['lower_limit']
		polar_upper_limit=request.POST['upper_limit']
		polar_graph(polar_function,polar_lower_limit,polar_upper_limit)
		return render(request,'polls/polar_output.html')
	else:
		return render(request,'polls/polar_input.html')
def z_as_yx(request):
	if request.method=="POST":
		z_as_yx_input=request.POST['yx_input']
		z_as_yx_plot(z_as_yx_input)
		return render(request,'polls/z_as_yx_output.html')
	else:
		return render(request,'polls/z_as_yx_input.html')

def y_as_x(request):
	if request.method=="POST":
		y_as_x_input=request.POST['y_as_x_input']
		lower_limit=float(request.POST['lower_limit'])
		upper_limit=float(request.POST['upper_limit'])
		# p3=plot(y_as_x_input,show=False)
		y_as_x_graph(y_as_x_input,lower_limit,upper_limit)
		return render(request,'polls/y_as_x_output.html')
	else:
		return render(request,'polls/y_as_x_input.html')
def histogram(request):
	if request.method=="POST":
		hist_file=request.FILES['hist_file']
		hist_file_title=request.POST['hist_file_title']
		hist_file_xlabel=request.POST['hist_file_xlabel']
		hist_file_ylabel=request.POST['hist_file_ylabel']
		data = pd.read_csv(hist_file, sep=',',header=None, index_col =0)
		fig_hist=hist_func(data,hist_file_title,hist_file_xlabel,hist_file_ylabel)
		return render(request,'polls/histogram_output.html',{'fig_hist':fig_hist})
	else:
		return render(request,'polls/histogram_input.html')

def piechart_input(request):
	if request.method=="POST":
		n=request.POST['piechart_input']
		vase_list=range(eval(n))
		return render(request,'polls/after_input.html',{'n':n,'vase_list':vase_list})
	else: 
		return render(request,'polls/give_input.html')
def graph(request):
	if request.method=="POST":
		number_forms=request.POST['number_forms']
		# x='0'
		# for i in range(int(number_forms)):
		# 	x=x+request.POST['after_input'+str(i+1)]
		ar2 = []
		ar3 = []
		for i in range(int(number_forms)):
			ar2.append(request.POST['after_input'+str(i+1)])
			ar3.append(0)
		sizes = ar2
		explode = ar3  # an array corresponding t which elemnts should be exploded. right now no element

		fig1, ax1 = plt.subplots()
		ax1.pie(sizes, explode=explode, autopct='%1.1f%%',shadow=True, startangle=90)
		ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
		plt.plot()
		fig1.savefig('polls/static/polls/pieplot.png')
		#js_data=json.dumps(mpld3.fig_to_dict(fig1))
		fig_html=mpld3.fig_to_html(fig1)
		plt.close()
		#mpld3.show()
		return render(request,'polls/graph.html',{'fig_html':fig_html})
	else:
		return HttpResponse("Not post method")

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #template=loader.get_template('polls/index.html')
    context={'latest_question_list':latest_question_list,}
    return render(request,'polls/index.html',context)

def detail(request, question_id):
    # try:
    question = get_object_or_404(Question,pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")

    return render(request, 'polls/detail.html', {'question': question})
def results(request, question_id):
    question=get_object_or_404(Question,pk=question_id)
    return render(request,'polls/results.html',{'question':question})
# ...
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
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))