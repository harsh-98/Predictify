from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import logout

def index(request):
	if request.user.is_authenticated:
		return render(request,'dashboard/index.html',{})
	else: 
		return HttpResponse("ERROR 404")

def logoutUser(request):
	logout(request)
	return redirect('/login/')