# -*- coding: utf-8 -*-
from django.core import serializers
from django.core.mail import send_mail
from django.http import JsonResponse
from django.shortcuts import render
from models import *
from django.core.mail import send_mail
from django.conf import settings
from django.views.decorators.cache import cache_page
from django.core.serializers.json import DjangoJSONEncoder
from django.core.paginator import Paginator


def home(request):
    banners = Banner.objects.all()
    abouts = About.objects.all()
    missions = Mission.objects.all()
    circles = Circle.objects.all()
    projects = Img_project.objects.filter(general=True, project_key__main=True)
    return render(request, "home.html", locals())


def projects(request):
    page = 1
    projects = Img_project.objects.filter(general=True)
    paginator = Paginator(projects, 4)
    project_pagi = paginator.page(page)
    categories = Category_project.objects.all()
    return render(request, "projects.html", locals())


def price(request, price_l='365'):
    prices = Price.objects.all()
    price_it = Price_item.objects.all()
    profit = Profit.objects.all()
    additational_cats = Price_add.objects.all()
    if price_l != '365':
        additational = Price_add.objects.get(id=price_l)
    print price_l
    return render(request, "price.html", locals())


def service(request):
    start_id = Service.objects.last()
    services = Service.objects.all().order_by('-id')
    service_current = Service.objects.last()
    print service_current
    return render(request, "service.html", locals())


def service_sort(request):
    cat = []
    data = request.POST
    print data['id']
    service_item = Service.objects.get(id=data['id'])
    cat = [{'head': service_item.head, 'text': service_item.text}]
    return JsonResponse(cat, safe=False)


def projects_pagi(request):
    cat = []
    data = request.POST
    print data['category']
    if data['category'] == 'all':
        projects = Img_project.objects.filter(general=True)
    else:
        projects = Img_project.objects.filter(general=True, project_key__category_id=data['category'])
    paginator = Paginator(projects, 4)
    project_pagi = paginator.page(data['page'])
    print project_pagi
    cat = [{'id': item.project_key_id, 'img': item.img.url, 'head_main': item.project_key.head, 'text': item.project_key.text} for item in project_pagi]
    print cat
    return JsonResponse(cat, safe=False)


def articles(request):
    page = 1
    article = Articles.objects.filter(general=True).order_by('-date')
    paginator = Paginator(article, 4)
    articles_pagi = paginator.page(page)
    categories = Articles_tag.objects.all()
    return render(request, "articles.html", locals())
