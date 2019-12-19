from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views.generic.base import View
from django.contrib.auth import logout as auth_logout
from api.models import *
from django.http import JsonResponse
# Create your views here.

from django.http import HttpResponse
from api.serializers import UserProfileSerializer
from frontend.forms import UserProfileForm, DeviceForm


class Home(View):
    def get(self, request, *args, **kwargs):
        context = {'message': 'Hello Django!'}
        return render(request, "index.html", context=context)




@login_required
def logout(request):
    """Logs out user"""
    auth_logout(request)
    return render_to_response('index.html', {}, RequestContext(request))

@login_required
def dashboard(request):
    context_dasboard = {'message': 'Hello dashboard!'}
    print(request.user.username)
    return render(request, "index.html", context=context_dasboard)

@login_required
def settings(request):
    context_dasboard = {'message': 'Hello settings!'}
    username = request.user.username
    # select profile with such username
    deviceForm = DeviceForm()
     #print(dict(request))
    return render(request, "index.html",{'deviceForm':deviceForm} )

