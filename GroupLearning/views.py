from django.shortcuts import render
from django_datatables_view.base_datatable_view import BaseDatatableView
from django.utils.html import escape
from django.db.models import Q
from .models import *
# Create your views here.


def mainpage(request):
    context = {}
    return render(request, 'index.html', context)

class learningclassview(BaseDatatableView):
    model = Name
    columns = ['id','col1','col2', 'col3']
    order_columns = ['id','col1','col2', 'col3']

    def render_column(self, row, column):
        return super(learningclassview, self).render_column(row, column)

    def filter_queryset(self, qs):
        search = self.request.GET.get('search[value]', None) 
        if search:
            qs = qs.filter(Q(col1__icontains=search) | Q(col2__icontains=search) | Q(col3__icontains=search) )
        return qs