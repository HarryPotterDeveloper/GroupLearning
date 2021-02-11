from django.urls import path, re_path
from .views import *
from django.views.generic import TemplateView

app_name = 'GroupLearning'

urlpatterns = [
    path('', mainpage , name='mainpage'),
    path('learningclassview/', learningclassview.as_view() , name='learningclassview'),
]

