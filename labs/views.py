# -*- encoding:utf8 -*-
from django.views.generic import TemplateView, ListView
from labs.forms import RegisterForm, LoginForm
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import render_to_response, get_object_or_404
from django.db.utils import IntegrityError
import json
import logging
from django.conf import settings
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import FormView
from django.utils.encoding import force_text
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.utils.decorators import method_decorator

logging.config.dictConfig(settings.LOGGING)
logger = logging.getLogger('file')

def home(request):    
    return render_to_response('tweeter/index.html',context_instance=RequestContext(request))    

def logout(request):
    logout(request)

class ProfileView(ListView):
    template_name = 'common/profile.html'
    def get_queryset(self):
        user = get_object_or_404(User, id__iexact=self.args[0])
        return user

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ProfileView, self).dispatch(*args, **kwargs)



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

        if not(form.errors):

            user = authenticate(username =in_dict_data['username'],password=in_dict_data['password'])

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
    template_name = 'common/register.html' #사용할 Template지정 
    form_class = RegisterForm              # Form Class   
    """
    위의 변수는 FormView의 Default변수들이고 아래 변수는 사용자 변수임.
    """
    success_url = 'success_register'       
    in_dict_data = {}


    def get_context_data(self, **kwargs):
        """
        이 Function은 get으로 접근시, 즉 최초에 접근시 호출이 되는 function임.
        context에는 form과 view class가 dict type으로 저장되어 있음.

        """
        context = super(RegisterFormView, self).get_context_data(**kwargs) 
        """
        아래에서 Form(html코드)을 context에 update하여 return함. 
        이때 form field에 대한 Validation html코드가 포함이 되어 return이 됨. 
        """
        context.update(form=RegisterForm(form_name='RegForm'))
        return context 

    def ajax(self, request):
        """
        form에서 submit을 하면 javascript에서 post방식으로 접근을 함.
        아래 post function을 거쳐서 ajax function으로 이동을 시킴. 
        """
        in_dict_data = json.loads(request.body)     # body에 dictionary type으로 전달이 됨. 
        form = self.form_class(data=in_dict_data)   # form을 구성을 함. 에러가 있는 지 확인함. 
        
        if not(form.errors):
            user = User(username=in_dict_data['username'], first_name=in_dict_data['firstname'], last_name=in_dict_data['lastname'])
            user.set_password(in_dict_data['password'])

            user.save()
            # profile은 django 1.5부터 사라짐. 
            # p = user.get_profile()
            # p.hobby = in_dict_data['hobby']
            # p.save()
        """
        json형태로 java script의 controller로 data를 return함. 
        """
        response_data = {'errors': form.errors, 'success_url': force_text(self.success_url)}        
        return HttpResponse(json.dumps(response_data), content_type="application/json")
            
    def post(self, request, **kwargs):    	       
        if request.is_ajax():
            return self.ajax(request)

        return super(RegisterFormView, self).post(request, **kwargs)
