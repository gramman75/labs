from rest_framework import serializers, viewsets
from board.models import Boards, Posts, Replies
from board.serializers import BoardSerializer, PostSerializer, ReplySerializer, BoardListSerializer, PaginationPostSerializer
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
# Create your views here.

class BoardViewSet(viewsets.ModelViewSet):
	queryset = Boards.objects.all()
	serializer_class = BoardSerializer

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
	
	def list(self, request):
		boardId = request.QUERY_PARAMS.get('boardId')

		print 'list boardId : %s' %(boardId)

		queryset = Posts.objects.filter(board__exact=boardId)
		paginator = Paginator(queryset, 3)

		page= request.QUERY_PARAMS.get('page')

		try:
			posts = paginator.page(page)
		except PageNotAnInteger:
			posts = paginator.page(1)
		except EmptyPage:
			posts = paginator.page(paginator.num_pages)

		serializer_context = {'request' : request}

		serializer = PaginationPostSerializer(instance=posts, context=serializer_context)
		return Response(serializer.data)

	def retrive(self, request, pk=None):
		boardId = request.QUERY_PARAMS['boardId']

		print 'retrive boardId : %s' %(boardId)

		queryset = Posts.objects.filter(board__exact=boardId)

		serializer  = PostSerializer(queryset)

		
		return Response(serializer.data)

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
