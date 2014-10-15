from django import forms
from djangular.forms import NgFormValidationMixin, NgModelFormMixin 
from djangular.styling.bootstrap3.forms import Bootstrap3FormMixin
from django.core.exceptions import ValidationError

def validate_username(value):
    # Just for demo. Do not validate passwords like this!
    if value.upper().count('FUCK'):
        raise ValidationError('Can not use "Fuck"') 

# class RegisterForm(NgFormValidationMixin, NgModelFormMixin, forms.Form):
class RegisterForm(NgModelFormMixin, NgFormValidationMixin, Bootstrap3FormMixin, forms.Form):	

	scope_prefix = 'subscribe_data'
	form_name = 'my_form'

	username = forms.CharField(max_length=10, min_length=5, validators=[validate_username])
	password = forms.CharField(widget=forms.PasswordInput, max_length=10, min_length=6)
	confirm  = forms.CharField(widget=forms.PasswordInput)
	email    = forms.EmailField()
	firstname = forms.CharField()
	lastname  = forms.CharField()
	hobby     = forms.CharField(required=False)

	def clean(self):
		if (self.cleaned_data.get('firstname') == 'Kim' and self.cleaned_data.get('lastname')=='MoonGeun'):
			raise ValidationError('The full name "John Doe" is rejected by the server.')

		return super(RegisterForm,self).clean()

    