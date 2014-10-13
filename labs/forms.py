from django import forms
from djangular.forms import NgFormValidationMixin, NgModelFormMixin 
from djangular.styling.bootstrap3.forms import Bootstrap3FormMixin

# class RegisterForm(NgFormValidationMixin, NgModelFormMixin, forms.Form):
class RegisterForm(NgModelFormMixin, NgFormValidationMixin, Bootstrap3FormMixin, forms.Form):	

	scope_prefix = 'subscribe_data'
	form_name = 'my_form'

	username = forms.CharField(max_length=10, min_length=3)
	password = forms.CharField()
	confirm  = forms.CharField()
	email    = forms.EmailField()
	firstname = forms.CharField()
	lastname  = forms.CharField()
	hobby     = forms.CharField(required=False)

    