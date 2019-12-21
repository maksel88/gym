from django.shortcuts import render
from django.template.response import TemplateResponse
from django.http import HttpResponse
from .forms import UserForm


def index(request):
    return TemplateResponse(request, " index.html")


def home(request):
    return TemplateResponse(request, 'person/home.html')
#
#
# def contact(request):
#     return HttpResponse('<h2>Контакты</h2>')


# def products(request, productid):
#     category = request.GET.get('cat', '')
#     output = '<h2>Product№ {0} Category: {1}</h2>'.format(productid, category)
#     return HttpResponse(output)
#
#
# def users(request):
#     id = request.GET.get('id', 1)
#     name = request.GET.get('name', 'Tom')
#     output = '<h2>User</h2><h3>id: {0} name: {1}</h3>'.format(id, name)
#     return HttpResponse(output)
