from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import logout
import subprocess
from .predictor import billu_scorer

def index(request):
	if request.user.is_authenticated:
		return render(request,'dashboard/form.html',{})
	else: 
		return HttpResponse("ERROR 404")

def logoutUser(request):
	logout(request)
	return redirect('/login/')

def predictScore(request):
	# data = ['F',15,'U','GT3','T',4,2,'health','services','home','mother',1,3,0,'no','yes','yes','yes','yes','yes','yes','yes',3,2,2,1,1,5,2,15,14]
	data = []
	data.append(request.POST.get('sex'))
	data.append(request.POST.get('age'))
	data.append(request.POST.get('address'))
	data.append(request.POST.get('famsize'))
	data.append(request.POST.get('Pstatus'))
	data.append(request.POST.get('Medu'))
	data.append(request.POST.get('Fedu'))
	data.append(request.POST.get('Mjob'))
	data.append(request.POST.get('Fjob'))
	data.append(request.POST.get('reason'))
	data.append(request.POST.get('guardian'))
	data.append(request.POST.get('traveltime'))
	data.append(request.POST.get('studytime'))
	data.append(request.POST.get('failures'))
	data.append(request.POST.get('schoolsup'))
	data.append(request.POST.get('famsup'))
	data.append(request.POST.get('paid'))
	data.append(request.POST.get('activities'))
	data.append(request.POST.get('nursery'))
	data.append(request.POST.get('higher'))
	data.append(request.POST.get('internet'))
	data.append(request.POST.get('romantic'))
	data.append(request.POST.get('famrel'))
	data.append(request.POST.get('freetime'))
	data.append(request.POST.get('goout'))
	data.append(request.POST.get('Dalc'))
	data.append(request.POST.get('Walc'))
	data.append(request.POST.get('health'))
	data.append(request.POST.get('absences'))
	data.append(request.POST.get('G1'))
	data.append(request.POST.get('G2'))
	# print(data)
	# print(type(data))

	graph_data = billu_scorer(data)
	# print(graph_data)
	# return HttpResponse('done')
	return render(request,'dashboard/index.html',{'line':graph_data['scores'],'pie1':graph_data['pie_charts'][0],'pie2':graph_data['pie_charts'][1],'average': graph_data['average'][0] })