from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from tweeter.views import TweetViewSet, UserViewSet, index 
from labs.views import RegisterFormView, LoginFormView
# from labs import NgFormDataValidView

router = DefaultRouter()
router.register(r'tweets',TweetViewSet)
router.register(r'users',UserViewSet)

urlpatterns = patterns('tweeter.views',
    # Examples:
    # url(r'^$', 'angDjango.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/',include(router.urls)),
    url(r'^$',index, name='index'),
)

urlpatterns += patterns('',
    url(r'^register/', RegisterFormView.as_view(), name='register'),
    url(r'^login/$',LoginFormView.as_view(), name='login')
    # url(r'^success_register/', NgFormDataValidView.as_view(), name='success_register'),

)
	