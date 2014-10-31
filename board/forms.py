from django.forms import ModelForm
from board.models import Posts

class PostForm(ModelForm):
	class Meta:
		model = Posts
		fields = ['id','board','title','contents','block','group','seq','level','createdBy','timestamp']
