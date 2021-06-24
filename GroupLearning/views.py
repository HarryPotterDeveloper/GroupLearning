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
from django.views.generic import ListView, DetailView 
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import Product
from .forms import ProductForm
# Create your views here.

@csrf_protect
def LoginForm(requset):
    context ={}
    if requset.user.is_authenticated:
        return HttpResponseRedirect('/product_list/')
    else :
        return render(requset,'./templates/CLoginForm.html',context)

@csrf_protect
def Login(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if request.user.is_authenticated:
        return HttpResponseRedirect('/product_list/')
    elif user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponseRedirect('/product_list/')
    else:
        return HttpResponseRedirect('/')



@csrf_protect
def logout_view(requset):
    auth.logout(requset)
    return HttpResponseRedirect("/")

def FirstPageView(requset):
    return render(requset,'./templates/FirstPage.html',{})
class ProductList(ListView): 
    model = Product

class ProductDetail(DetailView): 
    model = Product

class ProductCreate(SuccessMessageMixin, CreateView): 
    model = Product
    form_class = ProductForm
    success_url =reverse_lazy('GroupLearning:product_list')
    success_message = "Product successfully created!"

class ProductUpdate(SuccessMessageMixin, UpdateView): 
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('GroupLearning:product_list')
    success_message = "Product successfully updated!"

class ProductDelete(SuccessMessageMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('GroupLearning:product_list')
    success_message = "Product successfully deleted!"