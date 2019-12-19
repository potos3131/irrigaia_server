from django.conf.urls import include, url
from frontend import views

urlpatterns = [
    url('^$', views.Home.as_view() ),
    url('^logout/$',views.logout , name='logout'),
    url('^dashboard/$',views.dashboard , name='dashboard'),
    url('^settings/$', views.settings, name='settings'),


]

