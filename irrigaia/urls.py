"""irrigaia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin, auth
from api  import urls as urls_api
from weatherService import urls as urls_weather
from frontend import urls as urls_frontend
from rest_framework.authtoken.views import obtain_auth_token  #
from django.conf import settings
from django.conf.urls.static import static
#admin.autodiscover()
from django.conf.urls import url
from django.contrib import admin

from django.contrib.auth import views as auth_views
from django.contrib.auth import logout
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #api section
    url(r'^api/', include(urls_api)),
    #auth & register section
    url(r'^get-token/', obtain_auth_token, name='api_token_auth'),  #
    url('', include('social_django.urls', namespace='social')),
    # frontend section
    url(r'', include(urls_frontend)),

    # weather section
    #todo get data      url(r'^weather/last/', include('')),
    #todo get data      url(r'^weather/history/', include('')),
    #todo (post data)   url(r'^weather/', include('')),
    #todo : il faut etre loggé pour avoir la meteo (obtetnion lat lng)
    url(r'^weather/', include(urls_weather))
    #finish https://stackoverflow.com/questions/47065438/attributeerror-module-django-contrib-auth-views-has-no-attribute

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

#@todo : make a real allath manager see here https://www.geeksforgeeks.org/python-extending-and-customizing-django-allauth/
#https://www.youtube.com/watch?v=BiHSP6bTsrE
#Live Coding: Django AllAuth Package (OAuth2) https://www.youtube.com/watch?v=eXyTlHhHb3U