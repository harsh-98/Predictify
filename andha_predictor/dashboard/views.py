from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import logout
import subprocess
from .predictor import billu_scorer

def index(request):
	if request.user.is_authenticated:
		return render(request,'dashboard/index.html',{'line':[7,8,9],'pie1':[  2.87356322,   6.03448276,  63.2183908 ,  25.86206897,   2.01149425],'pie2':[  3.35249042,   8.33333333,  66.2835249 ,  16.76245211,   5.26819923],'average': 14})
	else: 
		return HttpResponse("ERROR 404")

def logoutUser(request):
	logout(request)
	return redirect('/login/')

def predictScore(request):
	data = ['F',15,'U','GT3','T',4,2,'health','services','home','mother',1,3,0,'no','yes','yes','yes','yes','yes','yes','yes',3,2,2,1,1,5,2,15,14]
	graph_data = billu_scorer(data)
	print(type(graph_data['pie_charts'][0]))
	return render(request,'dashboard/index.html',{'line':graph_data['scores'],'pie1':graph_data['pie_charts'][0],'pie2':graph_data['pie_charts'][1],'average': graph_data['average'][0] })
	# return HttpResponse("done")





