from rest_framework import serializers
from todo.models import Todo
from django.contrib.auth.models import User

class TodoSerializer(serializers.ModelSerializer):
	user = serializers.Field(source='user')

	class Meta:
		model = Todo
		fields = ('id', 'message', 'user','timestamp')

		