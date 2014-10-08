from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from tweeter import views

router = DefaultRouter()
router.register(r'tweets',views.TweetViewSet)
router.register(r'users',views.UserViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'angDjango.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/',include(router.urls)),
    url(r'^$',views.index, name='index'),
    url(r'^register/', views.RegisterFormView.as_view(),name="register"),
)
