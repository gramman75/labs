# from rest_framework import serializers
# from labs.models import Boards, Posts, Replies
# from django.contrib.auth.models import User

# class BoardSerializer(serializers.ModelSerializer):
# 	posts = PostSerializer(many=True, source='post_set')
	



# class PostSerializer(serializers.ModelSerializer):
# 	createdBy = serializers.Field(source='createdBy')
# 	board = serializers.Field(source='board')

# 	class Meta:
# 		model = Posts
# 		fields = ('board','title','contents','block','group','seq','level',//
# 			'createdBy','timestamp')


# class ReplySerializer(serializers.ModelSerializer):
# 	post = serializers.Field(source='post')
# 	createdBy = seriaalizers.Field(source='createdBy')

# 	class Meta:
# 		model = Replies
# 		fields = ('','')