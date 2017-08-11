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
	data.append(request.POST['sex'])
	data.append(request.POST['age'])
	data.append(request.POST['address'])
	data.append(request.POST['famsize'])
	data.append(request.POST['Pstatus'])
	data.append(request.POST['Medu'])
	data.append(request.POST['Fedu'])
	data.append(request.POST['Mjob'])
	data.append(request.POST['Fjob'])
	data.append(request.POST['reason'])
	data.append(request.POST['guardian'])
	data.append(request.POST['traveltime'])
	data.append(request.POST['studytime'])
	data.append(request.POST['failures'])
	data.append(request.POST['schoolsup'])
	data.append(request.POST['famsup'])
	data.append(request.POST['paid'])
	data.append(request.POST['activities'])
	data.append(request.POST['nursery'])
	data.append(request.POST['higher'])
	data.append(request.POST['internet'])
	data.append(request.POST['romantic'])
	data.append(request.POST['famrel'])
	data.append(request.POST['freetime'])
	data.append(request.POST['goout'])
	data.append(request.POST['Dalc'])
	data.append(request.POST['Walc'])
	data.append(request.POST['health'])
	data.append(request.POST['absences'])
	data.append(request.POST['G1'])
	data.append(request.POST['G2'])

	graph_data = billu_scorer(data)
	# print(type(graph_data['pie_charts'][0]))
	return render(request,'dashboard/index.html',{'line':graph_data['scores'],'pie1':graph_data['pie_charts'][0],'pie2':graph_data['pie_charts'][1],'average': graph_data['average'][0] })
	# return HttpResponse("done")





