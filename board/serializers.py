from rest_framework import serializers
from board.models import Boards, Posts, Replies
from django.contrib.auth.models import User

class ReplySerializer(serializers.ModelSerializer):
	# post = serializers.Field(source='post')
	createdBy = serializers.Field(source='createdBy')

	class Meta:
		model = Replies
		fields = ('id','post','contents','block','group','seq','level','createdBy','timestamp')

class PostSerializer(serializers.ModelSerializer):
	createdBy = serializers.Field(source='createdBy')	
	# replies = serializers.RelatedField(many=True)
	replies = ReplySerializer(many=True, read_only=True)

	class Meta:
		model = Posts
		fields = ('id','board','title','contents','block','group','seq','level','createdBy','timestamp', 'replies')		

class BoardSerializer(serializers.ModelSerializer):
	# posts = serializers.RelatedField(many=True)
	posts = PostSerializer(many=True, read_only=True) 

	class Meta:
		model = Boards
		fields = ('id','type','title','comment','startDate','endDate','enabled','timestamp','user','posts')					

class BoardListSerializer(serializers.ModelSerializer):
	class Meta:
		model = Boards
		fields = ('id','type','title','comment','startDate','endDate','enabled','timestamp','user')