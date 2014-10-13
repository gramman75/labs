from django.views.generic import TemplateView
from labs.forms import RegisterForm
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.db.utils import IntegrityError
import json
import logging
from django.conf import settings
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import FormView



logging.config.dictConfig(settings.LOGGING)
logger = logging.getLogger('file')


class RegisterFormView(FormView):
    template_name = 'common/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('form_data_valid')

    def get_context_data(self, **kwargs):
        context = super(RegisterFormView, self).get_context_data(**kwargs)
        context.update(RegForm=RegisterForm(form_name='RegForm'))
        return context	

    def post(self, request, *args, **kwargs):
    	# if not request.is_ajax():    		
    	# 	return HttpResponseBadRequest('Expected an XMLHttpRequest')
    	# console.lgo('1');
    	try:
            in_data = json.loads(request.body)
            bound_register_form = RegisterForm( form_name='RegForm',
                                                data={'username': in_data.get('username'),
                                                     'firstname' : in_data.get('firstname'),
                                                     'lastname' : in_data.get('lastname'),
                                                     'password' : in_data.get('password'),
                                                     'confirm'  : in_data.get('confirm'),
                                                     'email' : in_data.get('email'),
                                                     'hobby' : in_data.get('hobby')
                                                     });

            print 'valid form %s', bound_register_form.is_valid()



            if bound_register_form.is_valid():
                cd = bound_register_form.cleaned_data
                username = cd['username']
                firstname = cd['firstname']
                lastname = cd['lastname']
                password = cd['password']
                email    = cd['email']
                hobby    = cd['hobby']

                user = User(username=username, first_name=firstname, last_name=lastname)
                user.set_password(password)

                try:
                    user.save()
                except IntegrityError:
                    return HttpResponse('User Error')
                
                p = user.get_profile()
                p.hobby = hobby
                print in_data.get('hobby')
                p.save()
            
            print bound_register_form.form_name
            print bound_register_form.errors
            print bound_register_form
            logging.debug('form %s', bound_register_form)
            if bound_register_form.errors:                
                # return HttpResponse(bound_register_form);
                return super(SubscribeForm, self).clean()
                # return render_to_response('common/register.html', { 'RegForm' : bound_register_form})                
            else:
                return render_to_response('common/index.html', context_instance=RequestContext(request, user) )
        except:
            import sys
            print('uncaught!', sys.exc_info()[0], sys.exc_info()[1])
