from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def index(request):
	# return HttpResponse("<h1> Login Page </h1>")
	template = loader.get_template('login_register/index.html')
	context = {}
	# return HttpResponse(template.render(context,request))
	return render(request, 'login_register/index.html',context)

