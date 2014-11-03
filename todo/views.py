from django.shortcuts import render
from rest_framework import serializers
from todo.models import Todo
from rest_framework import viewsets
from todo.serializers import TodoSerializer
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
# Create your views here.

class TodoViewSet(viewsets.ModelViewSet):
	queryset = Todo.objects.all()
	serializer_class = TodoSerializer

	def pre_save(self,obj):
		obj.user = self.request.user

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(TodoViewSet, self).dispatch(*args, **kwargs)