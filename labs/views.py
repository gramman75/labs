# -*- encoding:utf8 -*-
from django.views.generic import TemplateView
from labs.forms import RegisterForm, LoginForm
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.db.utils import IntegrityError
import json
import logging
from django.conf import settings
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import FormView
from django.utils.encoding import force_text
from django.contrib.auth import authenticate, login


logging.config.dictConfig(settings.LOGGING)
logger = logging.getLogger('file')

class LoginFormView(FormView):
    template_name = 'common/login.html'
    form_class    = LoginForm
    success_url  = '/'

    def get_context_data(self, **kwargs): # get으로 접근시, 일반적으로 처음 화면 구성시 
        context = super(LoginFormView, self).get_context_data(**kwargs)
        context.update(form=LoginForm(form_name='LoginForm')) #form_name은 html의 <form name="value"> 값이 됨. 
        return context     

    def ajax(self, request):
        """
        Post에 의해서 연결이 됨.
        Form Base View의 경우 reqeust.body에서 form값을 전달 받아 Form을 구성하고
        Validation을 수행함.

        Error가 있을 경우 form.errors에 값이 들어감. 
        모든 Validation은 form에서 처리하게 되면 web화면에 에러 메세지를 보여줄수 있음.
        """
        in_dict_data = json.loads(request.body)
        form = self.form_class(data=in_dict_data)
        print in_dict_data
        print form.errors
        if not(form.errors):
            print 'pass'
            user = authenticate(username =in_dict_data['username'],password=['password'])

            if user is not None:
                login(request, user)                                

        response_data = {'errors': form.errors, 'success_url': force_text(self.success_url)}        
        return HttpResponse(json.dumps(response_data), content_type="application/json") 

    def post(self, request, **kwargs):  
        """
        submit에 의한 접근을 처리함.
        angular에 의해서 one page web을 구현하기 위해서 request에 is_ajax()를 이용하여 
        ajax()쪽은로 전달 함. 
        """
            
        if request.is_ajax():
            return self.ajax(request)

        return super(LoginFormView, self).post(request, **kwargs)

class RegisterFormView(FormView):
    template_name = 'common/register.html'
    form_class = RegisterForm
    success_url = 'success_register'
    in_dict_data = {}

    def get_context_data(self, **kwargs):
        context = super(RegisterFormView, self).get_context_data(**kwargs)
        context.update(form=RegisterForm(form_name='RegForm'))
        return context 

    
    def ajax(self, request):
        in_dict_data = json.loads(request.body)
        form = self.form_class(data=in_dict_data)
        print 'aaa'
        
        if not(form.errors):
            print 'bbb'
            user = User(username=in_dict_data['username'], first_name=in_dict_data['firstname'], last_name=in_dict_data['lastname'])
            user.set_password(in_dict_data['password'])

            user.save()

            # p = user.get_profile()
            # p.hobby = in_dict_data['hobby']
            # p.save()

        response_data = {'errors': form.errors, 'success_url': force_text(self.success_url)}        
        return HttpResponse(json.dumps(response_data), content_type="application/json")
            
    def post(self, request, **kwargs):    	       
        if request.is_ajax():
            return self.ajax(request)

        return super(RegisterFormView, self).post(request, **kwargs)
