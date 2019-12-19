from django.urls import path
from django.urls import re_path
from api import views

urlpatterns = [
    re_path(r'pixel/(?P<lat>[+-]?(\d*\.)?\d+),(?P<lon>[+-]?(\d*\.)?\d+)',views.Pixelview.as_view() ),
    re_path(r'weather/(?P<lat>[+-]?(\d*\.)?\d+),(?P<lon>[+-]?(\d*\.)?\d+)',views.Weatherview.as_view()),
    path('vegetables/list/', views.VegetableList.as_view()),
    path('vegetables/<int:pk>/', views.VegetableDetail.as_view()),
    path('vegetables/create/', views.VegetablePost.as_view()),
    path('device/create/',views.IrrigaiaDeviceViewset),
    # api version
    #
    # { "version_num":"0.1","version_name":"Berlin"}
    # todo     # login required
    path(r'version/', views.Version.as_view()),
]
