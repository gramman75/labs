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

def index(request):
	user = authenticate(username ='gramman75',password='kmk75042')
	if user is not None:
		login(request, user)
		return render(request,'tweeter/index.html')
	else:
		raise Http404()
		# return HttpResponse('<html><body>Error</body></html>') 


class TweetViewSet(viewsets.ModelViewSet):
	queryset = Tweet.objects.all()
	serializer_class = TweetSerializer
	def pre_save(self, obj):
		obj.user = self.request.user

class UserViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer




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