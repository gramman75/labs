from django import forms
from djangular.forms.angular_model import NgModelFormMixin 

class RegisterForm(NgModelFormMixin, forms.Form):
	username = forms.CharField(max_length=10, min_length=3)
	password = forms.CharField()
	confirm  = forms.CharField()
	email    = forms.EmailField()
	firstname = forms.CharField()
	lastname  = forms.CharField()
	hobby     = forms.CharField(required=False)

