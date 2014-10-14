from django import forms
from djangular.forms import NgFormValidationMixin, NgModelFormMixin 
from djangular.styling.bootstrap3.forms import Bootstrap3FormMixin
from django.core.exceptions import ValidationError

# class RegisterForm(NgFormValidationMixin, NgModelFormMixin, forms.Form):
class RegisterForm(NgModelFormMixin, NgFormValidationMixin, Bootstrap3FormMixin, forms.Form):	

	scope_prefix = 'subscribe_data'
	form_name = 'my_form'

	username = forms.CharField(max_length=10, min_length=5)
	password = forms.CharField()
	confirm  = forms.CharField()
	email    = forms.EmailField()
	firstname = forms.CharField()
	lastname  = forms.CharField()
	hobby     = forms.CharField(required=False)
	phone = forms.RegexField(r'^\+?[0-9 .-]{4,25}$', label='Phone number',
        error_messages={'invalid': 'Phone number have 4-25 digits and may start with +'})

	def clean(self):
		if (self.cleaned_data.get('firstname') == 'Kim' and self.cleaned_data.get('lastname')=='MoonGeun'):
			raise ValidationError('The full name "John Doe" is rejected by the server.')

		return super(RegisterForm,self).clean()

    