from rest_framework import serializers
from tweeter.models import Tweet
from django.contrib.auth.models import User

class TweetSerializer(serializers.ModelSerializer):
	user = serializers.Field(source='user')

	class Meta:
		model = Tweet
		fields = ('text','user','timestamp')
	

class UserSerializer(serializers.ModelSerializer):
	tweets = TweetSerializer(many=True, source='tweet_set')
	class Meta:
		model = User
		fields = ('username','first_name','tweets')	