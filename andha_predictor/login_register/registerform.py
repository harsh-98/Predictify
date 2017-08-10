from django import forms

class registerForm(forms.Form):
	first_name = forms.CharField(required = True, max_length = 30)
	last_name = forms.CharField(required = True, max_length = 30)
	email = forms.EmailField(required = True)
	password = forms.CharField(required = True)
	username = forms.CharField(required = True)

class loginForm(forms.Form):
	username = forms.CharField( required = True)
	password = forms.CharField(required = True)
