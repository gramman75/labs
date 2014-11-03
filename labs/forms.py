# -*-encoding:utf8 -*-
from django import forms
from djangular.forms import NgFormValidationMixin, NgModelFormMixin 
from djangular.styling.bootstrap3.forms import Bootstrap3FormMixin
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

def validate_username(value):	
	if value.upper().count('FUCK'):
		raise ValidationError('Can not use "Fuck"') 
    # if User.objects.get(username=value):
    # 	raise ValidationError('%s username already used' %value)   

class LEDForm(NgModelFormMixin, NgFormValidationMixin, Bootstrap3FormMixin, forms.Form):
	scope_prefix = 'led_data'
	form_name    = 'led_form'

	red   = forms.DecimalField(min_value=0, max_value=255, max_digits=3, initial=0)
	green = forms.DecimalField(min_value=0, max_value=255, max_digits=3, initial=0)
	blue  = forms.DecimalField(min_value=0, max_value=255, max_digits=3, initial=0)

	# def clean_red(self):
	# 	data = self.cleaned_data['red']
	# 	if not(data.isdigit()):
	# 		raise ValidationError("Only Number");
	# 	elif (int(data) <0 or int(data) > 255 ):
	# 		raise ValidationError("Only Number('0 ~ 255')")

	



class LoginForm(NgModelFormMixin, NgFormValidationMixin, Bootstrap3FormMixin, forms.Form):
	scope_prefix = 'login_data'
	form_name	 = 'login_form'

	username = forms.CharField(max_length=10, min_length=5);
	password = forms.CharField(widget=forms.PasswordInput)
	rememmberme = forms.CharField(widget=forms.CheckboxInput)

	def clean(self):
		if not(authenticate(username=self.cleaned_data.get('username'),password=self.cleaned_data.get('password'))):		
			raise ValidationError('id/password incorrect')			
   	
class RegisterForm(NgModelFormMixin, NgFormValidationMixin, Bootstrap3FormMixin, forms.Form):	

	scope_prefix = 'subscribe_data' #Form의 개발 Value를 하나씩 받지 않고 전체를 받기 위함.
	form_name = 'my_form'           #html의 form tag에서 form_name의 값이 됨. 

	"""
	Validators 속성을 이용하여 해당 Field에 대한 Form Valdation을 적용할 수 있음. 
	"""
	username = forms.CharField(initial ='aaaaaaa', max_length=10, min_length=5, validators=[validate_username]) 
	password = forms.CharField(initial ='123456', widget=forms.PasswordInput, max_length=10, min_length=6)
	confirm  = forms.CharField(initial = '123456', widget=forms.PasswordInput)
	email    = forms.EmailField(initial ='gramman75@gmail.com')
	firstname = forms.CharField(initial ='moon')
	lastname  = forms.CharField(initial = 'geun')
	hobby     = forms.CharField(required=False)

	"""
	Validators속성이 해당 필드에 대한 Validation을 수행한는 것이라면 clean function은 form 전체에 대한 Validation을 수행.
	다른 Field와의 Validation이 필요할 때 사용 함.
	"""
	def clean(self):
		if (self.cleaned_data.get('firstname') == 'Kim' and self.cleaned_data.get('lastname')=='MoonGeun'):
			raise ValidationError('The full name "John Doe" is rejected by the server.')
		if (self.cleaned_data.get('password') != self.cleaned_data.get('confirm')):
			raise ValidationError('패스워드가 일치하지 않습니다. 다시 입력해주세요.')
		return super(RegisterForm,self).clean()


 

    