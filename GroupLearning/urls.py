from django import urls
from django.contrib import admin
from django.urls import path, re_path
from .views import *
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings
from . import views


app_name = 'GroupLearning'

urlpatterns = [
    path('admin/',admin.site.urls),
    path('',LoginForm),
    path('login/',Login),
    path('accounts/login/', Login),
    path('logout_view/', logout_view),
    path('accounts/logout/', logout_view , name='logout'),
    

    path('FirstPageView/', FirstPageView, name='FirstPageView'),
    # path('hr_db_method/', login_required(FirstPageView.hr_db_method), name='hr_db_method'),
    # path('migration/', login_required(FirstPageView.migration), name='migration'),

    # path('PersonnelPaymentView/', login_required(PersonnelPaymentView.as_view()), name='PersonnelPaymentView'),
    # path('get_personnel_data/', login_required(PersonnelPaymentView.get_personnel_data), name='get_personnel_data'),
    # path('SendToKarposhe/', login_required(PersonnelPaymentView.SendToKarposhe), name='SendToKarposhe'),
    path('product_list/', views.ProductList.as_view(), name='product_list'),
    path('view/<int:pk>', views.ProductDetail.as_view(), name='product_view'),
    path('new', views.ProductCreate.as_view(), name='product_new'),
    path('edit/<int:pk>', views.ProductUpdate.as_view(), name='product_edit'),
    path('delete/<int:pk>', views.ProductDelete.as_view(), name='product_delete')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

