# -*- coding: utf-8 -*-
from django.core import serializers
from django.core.mail import send_mail
from django.http import JsonResponse
from django.shortcuts import render
from solar.models import *
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
    first_ard = Contacts.objects.first()
    phones = Phone.objects.filter(contact_key=first_ard.id)
    email = Email.objects.filter(contact_key=first_ard.id)
    partners = Partner.objects.all()
    massage_form = Form_cont_main.objects.filter(form_name='message').first()
    call_form = Form_cont_main.objects.filter(form_name='call').first()
    return render(request, "home.html", locals())


def projects(request, order, page_pr):
    if order == 'all':
        projects = Img_project.objects.filter(general=True)
    else:
        projects = Img_project.objects.filter(project_key__category_id=order).order_by('-id')
    if order != 'all':
        categor_all_flag = 'hidden'
    else:
        categor_id_flag = 'hidden'
    gallery = Project_main.objects.first()
    paginator = Paginator(projects, 4)
    project_pagi = paginator.page(page_pr)
    categories = Category_project.objects.all()
    first_ard = Contacts.objects.first()
    phones = Phone.objects.filter(contact_key=first_ard.id)
    email = Email.objects.filter(contact_key=first_ard.id)
    massage_form = Form_cont_main.objects.filter(form_name='form').first()
    call_form = Form_cont_main.objects.filter(form_name='call').first()
    return render(request, "projects.html", locals())


def price(request, price_l='365'):
    gallery = Price_main.objects.first()
    prices = Price.objects.all()
    price_it = Price_item.objects.all()
    profit = Profit.objects.all()
    additational_cats = Price_add.objects.all()
    if price_l != '365':
        additational = Price_add.objects.get(id=price_l)
    print (price_l)
    first_ard = Contacts.objects.first()
    phones = Phone.objects.filter(contact_key=first_ard.id)
    email = Email.objects.filter(contact_key=first_ard.id)
    massage_form = Form_cont_main.objects.filter(form_name='form').first()
    call_form = Form_cont_main.objects.filter(form_name='call').first()
    return render(request, "price.html", locals())


def service(request):
    gallery = Service_main.objects.first()
    start_id = Service.objects.last()
    services = Service.objects.all().order_by('-id')
    service_current = Service.objects.last()
    print (service_current)
    first_ard = Contacts.objects.first()
    phones = Phone.objects.filter(contact_key=first_ard.id)
    email = Email.objects.filter(contact_key=first_ard.id)
    massage_form = Form_cont_main.objects.filter(form_name='form').first()
    call_form = Form_cont_main.objects.filter(form_name='call').first()
    return render(request, "service.html", locals())


def service_sort(request):
    cat = []
    data = request.POST
    print (data['id'])
    service_item = Service.objects.get(id=data['id'])
    cat = [{'head': service_item.head, 'text': service_item.text}]
    return JsonResponse(cat, safe=False)


def projects_pagi(request):
    cat = []
    data = request.POST
    print (data['category'])
    if data['category'] == 'all':
        projects = Img_project.objects.filter(general=True)
    else:
        projects = Img_project.objects.filter(general=True, project_key__category_id=data['category'])
    paginator = Paginator(projects, 4)
    project_pagi = paginator.page(data['page'])
    cat = [{'id': item.project_key_id, 'img': item.img.url, 'head_main': item.project_key.head, 'text': item.project_key.text} for item in project_pagi]
    return JsonResponse(cat, safe=False)


def articles(request, order, page_art):
    gallery = Article_main.objects.first()
    if order == 'all':
        article = Articles.objects.filter(general=True).order_by('-date')
    else:
        article = Articles.objects.filter(tag_key_id=order).order_by('-date')
    if order != 'all':
        categor_all_flag = 'hidden'
    else:
        categor_id_flag = 'hidden'
    paginator = Paginator(article, 5)
    articles_pagi = paginator.page(page_art)
    categories = Articles_tag.objects.all()
    first_ard = Contacts.objects.first()
    phones = Phone.objects.filter(contact_key=first_ard.id)
    email = Email.objects.filter(contact_key=first_ard.id)
    massage_form = Form_cont_main.objects.filter(form_name='form').first()
    call_form = Form_cont_main.objects.filter(form_name='call').first()
    return render(request, "articles.html", locals())


def contact(request):
    first_ard = Contacts.objects.first()
    contacts_obj = Contacts.objects.get(id=first_ard.id)
    adress = Adres.objects.filter(contact_key=first_ard.id)
    phones = Phone.objects.filter(contact_key=first_ard.id)
    email = Email.objects.filter(contact_key=first_ard.id)
    massage_form = Form_cont_main.objects.filter(form_name='form').first()
    call_form = Form_cont_main.objects.filter(form_name='call').first()
    return render(request, "contact.html", locals())


def mass(request):
    print (request.POST)
    data = request.POST
    phone = data.get('feed-phone')
    link = data.get('feed-link')
    send_mail(
        "Вам оставили контакты для обратной связи",
        phone + "\n" + "Page of site" + " " + "www.cdc.energy" + link,
        settings.EMAIL_HOST_USER,
        ['maxkaliberda1@gmail.com',],
        fail_silently=False
    )
    cat = []
    text_data = Form_cont_main.objects.filter(form_name='call').first()
    print (text_data.text_ans)
    cat = [{'text_data': text_data.text_ans}]
    print (cat)
    return JsonResponse(cat, safe=False)


def massgen(request):
    print (request.POST)
    data = request.POST
    phone = data.get('form-phone')
    name = data.get('form-name')
    email = data.get('form-email')
    subject = data.get('form-subject')
    message = data.get('form-message')
    send_mail(
        "Вам оставили контакты для обратной связи",
        phone + "\n" + email + "\n" + subject + "\n" + message,
        settings.EMAIL_HOST_USER,
        ['maxkaliberda1@gmail.com', ],
        fail_silently=False
    )
    cat = []
    text_data = Form_cont_main.objects.filter(form_name='message').first()
    print (text_data.text_ans)
    cat = [{'text_data': text_data.text_ans}]
    print (cat)
    return JsonResponse(cat, safe=False)
