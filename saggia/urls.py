from django.conf.urls import patterns, url
from saggia import views

urlpatterns = patterns('',
    url(r'^index/$', views.index, name='index'),
    url(r'^user/(?P<uname>\w+)/$', views.user, name='user'),
    #url(r'^user/(?P<uname>\w+)/invite/$', views.invite, name='user'),
    url(r'^user/$', views.user, name='user'),
    url(r'^$', views.first, name='first'),
    url(r'^login$', views.login_view, name='login'),
    url(r'^error$', views.error, name='error'),
    url(r'^logout$', views.logout_view, name='logout'), 
)
