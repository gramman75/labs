from rest_framework import serializers, viewsets
from board.models import Boards, Posts, Replies
from board.serializers import BoardSerializer, PostSerializer, ReplySerializer, BoardListSerializer
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
# Create your views here.

class BoardViewSet(viewsets.ModelViewSet):
	# queryset = Boards.objects.all()
	serializer_class = PostSerializer

	def get_queryset(self):
		print self.kwargs
		queryset = Posts.objects.filter(board__exact=self.kwargs['pk'])

		return queryset

	def pre_save(self, obj):
		obj.user = self.request.user

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(BoardViewSet, self).dispatch(*args, **kwargs)

class PostViewSet(viewsets.ModelViewSet):
	queryset = Posts.objects.all()
	serializer_class = PostSerializer

	def pre_save(self, obj):
		obj.createdBy = self.request.user

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(PostViewSet,self).dispatch(*args, **kwargs)


class ReplyViewSet(viewsets.ModelViewSet):
	queryset = Replies.objects.all()
	serializer_class = ReplySerializer

	def pre_save(self, obj):
		obj.createdBy = self.request.user

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(ReplyViewSet,self).dispatch(*args, **kwargs)	

class BoardListViewSet(viewsets.ModelViewSet):
	queryset = Boards.objects.all()
	serializer_class = BoardListSerializer	
