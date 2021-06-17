from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django_datatables_view.base_datatable_view import BaseDatatableView
from django.views.decorators.csrf import csrf_protect
from django.utils.html import escape
from django.http import Http404, HttpResponse, HttpResponseRedirect, JsonResponse
from django.db.models import Q
from django.urls import reverse
from django.contrib import auth
from .models import *
# Create your views here.

@csrf_protect
def LoginForm(requset):
    context ={}
    if requset.user.is_authenticated:
        return HttpResponseRedirect('/FirstPageView/')
    else :
        return render(requset,'./templates/CLoginForm.html',context)

@csrf_protect
def Login(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if request.user.is_authenticated:
        return HttpResponseRedirect('/FirstPageView/')
    elif user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponseRedirect('/FirstPageView/')
    else:
        return HttpResponseRedirect('/')



@csrf_protect
def logout_view(requset):
    auth.logout(requset)
    return HttpResponseRedirect("/")

def FirstPageView(requset):
    return render(requset,'./templates/FirstPage.html',{})
