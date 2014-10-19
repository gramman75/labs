# -*-encoding:utf8 -*-
from django import forms
from djangular.forms import NgFormValidationMixin, NgModelFormMixin 
from djangular.styling.bootstrap3.forms import Bootstrap3FormMixin
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

def validate_username(value):
    # Just for demo. Do not validate passwords like this!
    if value.upper().count('FUCK'):
        raise ValidationError('Can not use "Fuck"') 
    if User.objects.get(username=value):
    	raise ValidationError('%s username already used' %value)    
    	
class RegisterForm(NgModelFormMixin, NgFormValidationMixin, Bootstrap3FormMixin, forms.Form):	

	scope_prefix = 'subscribe_data'
	form_name = 'my_form'

	username = forms.CharField(initial ='aaaaaaa', max_length=10, min_length=5, validators=[validate_username])
	password = forms.CharField(initial ='123456', widget=forms.PasswordInput, max_length=10, min_length=6)
	confirm  = forms.CharField(initial = '123456', widget=forms.PasswordInput)
	email    = forms.EmailField(initial ='gramman75@gmail.com')
	firstname = forms.CharField(initial ='moon')
	lastname  = forms.CharField(initial = 'geun')
	hobby     = forms.CharField(required=False)

	def clean(self):
		if (self.cleaned_data.get('firstname') == 'Kim' and self.cleaned_data.get('lastname')=='MoonGeun'):
			raise ValidationError('The full name "John Doe" is rejected by the server.')
		if (self.cleaned_data.get('password') != self.cleaned_data.get('confirm')):
			raise ValidationError('패스워드가 일치하지 않습니다. 다시 입력해주세요.')
		return super(RegisterForm,self).clean()

    