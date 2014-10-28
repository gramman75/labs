from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from rest_framework import viewsets
from tweeter.models import Tweet
from tweeter.serializers import TweetSerializer, UserSerializer
from django.http import Http404
import json
from django.http import HttpResponseBadRequest, HttpResponse
from django.contrib.auth.decorators import login_required
from rest_framework import permissions
from django.utils.decorators import method_decorator

# def index(request):
# 	# user = authenticate(username ='gramman75',password='kmk75042')
# 	if request.user.is_authenticated():
# 		print 'login'
# 		print request.user
# 	else:
# 		print 'out'

# 	return render(request,'tweeter/index.html')
# 	# if user is not None:
# 	# 	login(request, user)
# 	# 	return render(request,'tweeter/index.html')
# 	# else:
# 	# 	raise Http404()
# 	# 	# return HttpResponse('<html><body>Error</body></html>') 

class TweetViewSet(viewsets.ModelViewSet):

	queryset = Tweet.objects.all()
	serializer_class = TweetSerializer
	# permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
	# permissions.classes = [ permissions.AllowAny]
	
	def pre_save(self, obj):
		obj.user = self.request.user
	
	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(TweetViewSet, self).dispatch(*args, **kwargs)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	# permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
	# permissions.classes = [permissions.AllowAny]

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(UserViewSet, self).dispatch(*args, **kwargs)


    	# console.log(in_data.get('username'))

# def register(request):
# 	return render_to_response('register.html')
# def register(request):
# 	if request.method == "POST":
# 		form = RegisterForm(request.POST)
# 		if form.is_valid():
# 			pass

# 		if form.errors:
# 			return render_to_response('register.html',{ 'form':form})




# Create your views here.
