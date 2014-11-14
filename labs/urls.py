# -*-encoding:utf8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from tweeter.views import TweetViewSet, UserViewSet 
from labs.views import RegisterFormView, LoginFormView, home, ProfileView, LEDFormView, TemperatureView, testAjax
from todo.views import TodoViewSet
from board.views import PostViewSet, ReplyViewSet, BoardListViewSet, BoardViewSet
from ncd.views import SamSkillViewSet, SamEmployeeViewSet, SamJobLevelViewSet, SamDivisionViewSet, SamDepartmentViewSet, EmployeeDetailView
# from labs import NgFormDataValidView

# from django.contrib.auth.views import login, logout

router = DefaultRouter()

router.register(r'tweets',TweetViewSet)
router.register(r'users',UserViewSet)
router.register(r'todos',TodoViewSet)
router.register(r'boards',BoardViewSet)
router.register(r'posts',PostViewSet)
router.register(r'replies',ReplyViewSet)
router.register(r'boardList',BoardListViewSet)

router.register(r'samskills',SamSkillViewSet)
router.register(r'samemployees',SamEmployeeViewSet)
router.register(r'samjoblevels',SamJobLevelViewSet)
router.register(r'samdivisions',SamDivisionViewSet)
router.register(r'samdepartments',SamDepartmentViewSet)

urlpatterns = patterns('tweeter.views',
    # Examples:
    # url(r'^$', 'angDjango.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/',include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls',namespace='rest_framework')),
)

urlpatterns += patterns('',
    # form template을 return받기 위한 url. url은 app.js의 state에서 정의한 url과 같아야 함.
    url(r'^register/', RegisterFormView.as_view(), name='register'),
    url(r'^login/',LoginFormView.as_view(), name='login'),
    url(r'^logout/$','django.contrib.auth.views.logout',{'next_page' : '/'}),
    url(r'^profile/(\d)/',ProfileView.as_view(), name='profile'),
    url(r'^led/$',LEDFormView.as_view(), name='led'),
    url(r'^temperature/$', TemperatureView.as_view(), name='temperature'),
    url(r'^$',home, name='home'),         
    url(r'^testAjax/$', testAjax, name='testAjax'),
    url(r'^employeeDetail/$', EmployeeDetailView.as_view(), name='employeeDetail'),
    # url(r'^employeeDetail/(?P<pk>\d)/$', EmployeeDetailView.as_view(), name='employeeDetail'),
    # url(r'^success_register/', NgFormDataValidView.as_view(), name='success_register'),
)

urlpatterns += patterns('',
    url("", include('django_socketio.urls'))
)	


urlpatterns += patterns("chat.views",
    url("^rooms/$", "rooms", name="rooms"),
    url("^create/$", "create", name="create"),
    url("^system_message/$", "system_message", name="system_message"),
    url("^rooms/(?P<slug>.*)$", "room", name="room"),
)
