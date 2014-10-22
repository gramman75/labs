from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from tweeter.views import TweetViewSet, UserViewSet 
from labs.views import RegisterFormView, LoginFormView, home, ProfileView
# from labs import NgFormDataValidView
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.views import login, logout

router = DefaultRouter()

router.register(r'tweets',TweetViewSet)
router.register(r'users',UserViewSet)

urlpatterns = patterns('tweeter.views',
    # Examples:
    # url(r'^$', 'angDjango.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/',include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls',namespace='rest_framework')),
)

urlpatterns += patterns('',
    url(r'^register/', RegisterFormView.as_view(), name='register'),
    url(r'^login/',LoginFormView.as_view(), name='login'),
    url(r'^logout/$','django.contrib.auth.views.logout',{'next_page' : '/'}),
    url(r'^profile/(\d)/',ProfileView.as_view(), name='profile'),

    url(r'^$',home, name='home'),         
    # url(r'^accounts/login/$', LoginFormView.as_view(), name='login'),    
    # url(r'^success_register/', NgFormDataValidView.as_view(), name='success_register'),

)
	