# -*- encoding:utf8 -*-
from django.shortcuts import render
from rest_framework import viewsets
from ncd.models import SamSkill, SamEmployee, SamJobLevel, SamDivision, SamDepartment
from ncd.serializers import SamSkillSerializer, SamEmployeeSerializer
from ncd.serializers import SamJobLevelSerializer, SamDivisionSerializer, SamDepartmentSerializer
from ncd.forms import EmployeeForm
from rest_framework.response import Response
from django.views.generic.edit import FormView

# Create your views here.

class SamSkillViewSet(viewsets.ModelViewSet):
	queryset = SamSkill.objects.all()
	serializer_class = SamSkillSerializer

class SamJobLevelViewSet(viewsets.ModelViewSet):
	queryset = SamJobLevel.objects.all()
	serializer_class = SamJobLevelSerializer

class SamDivisionViewSet(viewsets.ModelViewSet):
	queryset = SamDivision.objects.all()
	serializer_class = SamDivisionSerializer

class SamDepartmentViewSet(viewsets.ModelViewSet):
	queryset = SamDepartment.objects.all()
	serializer_class = SamDepartmentSerializer

class SamEmployeeViewSet(viewsets.ModelViewSet):
	queryset = SamEmployee.objects.all()
	serializer_class = SamEmployeeSerializer

	def list(self, requeset):
		skill = requeset.QUERY_PARAMS.get('skill')
		print 'skill %s' %skill
		queryset = SamEmployee.objects.filter(skill_code__exact=skill)
		serializer = SamEmployeeSerializer(queryset, many=True)

		return Response(serializer.data)

# def employeeDetail(request, id):
# 	if request.method == 'GET':
# 		employee = SamEmployee.objects.get(pk=id)
# 		form = EmployeeForm(instance=employee)

# 	 	return render(request, 'ncd/employeeDetail.html',{'form' : form })
# 	elif request.method == 'POST':
# 		form = EmployeeForm(data=request.POST)
# 		form.save()

# 		return render(request, 'ncd/employeeDetail.html',{'form' : form })

class EmployeeDetailView(FormView):
	template_name = 'ncd/employeeDetail.html'
	form_class    = EmployeeForm

	in_dict_data = {}

	def get_context_data(self, **kwargs):		
		id =  self.request.GET['id']
		context = super(EmployeeDetailView, self).get_context_data(**kwargs)
		emp = SamEmployee.objects.get(pk=id)
		form = self.form_class(instance=emp,form_name='form')
		# context.update(form=EmployeeForm(form_name='form'))
		context.update(form=form)

		return context

	def ajax(self, request):   
		in_dict_data = json.loads(request.body)     # body에 dictionary type으로 전달이 됨. 
		form = self.form_class(data=in_dict_data)   # form을 구성을 함. 에러가 있는 지 확인함. 
        
		if not(form.errors):
			user = User(username=in_dict_data['username'], first_name=in_dict_data['firstname'], last_name=in_dict_data['lastname'])
          
		response_data = {'errors': form.errors, 'success_url': force_text(self.success_url), 'form' : form}        
		return HttpResponse(json.dumps(response_data), content_type="application/json")
            
	def post(self, request, **kwargs):    	       
		if request.is_ajax():
			return self.ajax(request)

		return super(EmployeeDetailView, self).post(request, **kwargs)

	
