# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


# Create your models here.


class Banner(models.Model):
    head = models.CharField(max_length=500, null=True, blank=True)
    text = models.CharField(max_length=1000, null=True, blank=True)
    text_button = models.CharField(max_length=500, null=True, blank=True)
    img = models.ImageField(blank=True)
    first = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s' % self.head

    class Meta:
        db_table = 'banner'
        verbose_name = 'Баннер'
        verbose_name_plural = 'Баннеры'


class About(models.Model):
    head = models.CharField(max_length=500, null=True, blank=True)
    text = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return '%s' % self.head

    class Meta:
        db_table = 'about'
        verbose_name = 'О_нас'
        verbose_name_plural = 'О_нас'


class Mission(models.Model):
    head = models.CharField(max_length=500, null=True, blank=True)
    text = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return '%s' % self.head

    class Meta:
        db_table = 'mission'
        verbose_name = 'Миссия'
        verbose_name_plural = 'Миссия'


class Circle(models.Model):
    count = models.IntegerField(null=True, blank=True)
    head = models.CharField(max_length=500, null=True, blank=True)
    text = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return '%s' % self.head

    class Meta:
        db_table = 'circle'
        verbose_name = 'Цыфра'
        verbose_name_plural = 'Цыфры'


class Category_project(models.Model):
    head = models.CharField(max_length=500, null=True, blank=True)

    def __unicode__(self):
        return '%s' % self.head

    class Meta:
        db_table = 'category_project'
        verbose_name = 'Категория_проекты'
        verbose_name_plural = 'Категории_проекты'


class Project(models.Model):
    head = models.CharField(max_length=500, null=True, blank=True)
    category = models.ForeignKey(Category_project, null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    main = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s' % self.head

    class Meta:
        db_table = 'project'
        verbose_name = 'Проект'
        verbose_name_plural = 'Проеткы'


class Img_project(models.Model):
    project_key = models.ForeignKey(Project, null=True, blank=True)
    head = models.CharField(max_length=500, null=True, blank=True)
    img = models.ImageField(null=True, blank=True)
    general = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s' % self.head

    class Meta:
        db_table = 'img_project'
        verbose_name = 'Картинка_проекты'
        verbose_name_plural = 'Картинки_проекты'


class Partner(models.Model):
    head = models.CharField(max_length=500, null=True, blank=True)
    text = models.CharField(max_length=500, null=True, blank=True)
    img = models.ImageField(null=True, blank=True)

    def __unicode__(self):
        return '%s' % self.head

    class Meta:
        db_table = 'Partner'
        verbose_name = 'Партнер'
        verbose_name_plural = 'Партнеры'


class Service(models.Model):
    head = models.CharField(max_length=500, null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    main = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s' % self.head

    class Meta:
        db_table = 'Service'
        verbose_name = 'Сервис'
        verbose_name_plural = 'Сервисы'


class Img_Service(models.Model):
    Service_key = models.ForeignKey(Service, null=True, blank=True)
    head = models.CharField(max_length=500, null=True, blank=True)
    img = models.ImageField(null=True, blank=True)
    general = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s' % self.head

    class Meta:
        db_table = 'img_Service'
        verbose_name = 'Картинка_сервис'
        verbose_name_plural = 'Картинки_сервисы'


class Price(models.Model):
    head = models.CharField(max_length=500, null=True, blank=True)
    text = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return '%s' % self.head

    class Meta:
        db_table = 'Price'
        verbose_name = 'Цена'
        verbose_name_plural = 'Цены'


class Price_item(models.Model):
    price_key = models.ForeignKey(Price, null=True, blank=True)
    power = models.CharField(max_length=500, null=True, blank=True)
    price = models.CharField(max_length=500, null=True, blank=True)

    def __unicode__(self):
        return '%s' % self.price_key.head

    class Meta:
        db_table = 'Price_item'
        verbose_name = 'Цена_м'
        verbose_name_plural = 'Цены_м'


class Profit(models.Model):
    price_key = models.ForeignKey(Price, null=True, blank=True)
    profit = models.CharField(max_length=1000, null=True, blank=True)

    def __unicode__(self):
        return '%s' % self.price_key.head

    class Meta:
        db_table = 'Profit'
        verbose_name = 'Доход'
        verbose_name_plural = 'Доходы'


class Price_add(models.Model):
    head = models.CharField(max_length=1000, null=True, blank=True)
    text = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return '%s' % self.head

    class Meta:
        db_table = 'Price_add'
        verbose_name = 'Цены_доп_инфо'
        verbose_name_plural = 'Цены_доп_инфо'


class Articles_tag(models.Model):
    head = models.CharField(max_length=1000, null=True, blank=True)

    def __unicode__(self):
        return '%s' % self.head

    class Meta:
        db_table = 'Articles_tag'
        verbose_name = 'Тег_к_статьям'
        verbose_name_plural = 'Теги_к_статьям'


class Articles(models.Model):
    head = models.CharField(max_length=1000, null=True, blank=True)
    tag_key = models.ForeignKey(Articles_tag, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    general = models.BooleanField(default=False)
    text = models.TextField(blank=True, null=True)
    facebook_link = models.CharField(max_length=1000, null=True, blank=True)
    img = models.ImageField(blank=True, null=True)

    def __unicode__(self):
        return '%s' % self.head

    class Meta:
        db_table = 'Articles'
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class Contacts(models.Model):
    head = models.CharField(max_length=1000, null=True, blank=True)
    text = models.CharField(max_length=2000, null=True, blank=True)
    img_back = models.ImageField(null=True, blank=True)

    def __unicode__(self):
        return '%s' % self.head

    class Meta:
        db_table = 'Contact'
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'


class Project_main(models.Model):
    head = models.CharField(max_length=1000, null=True, blank=True)
    text = models.CharField(max_length=2000, null=True, blank=True)
    img_back = models.ImageField(null=True, blank=True)

    def __unicode__(self):
        return '%s' % self.head

    class Meta:
        db_table = 'Project_main'
        verbose_name = 'Страничка_проектов'
        verbose_name_plural = 'Страничка_проектов'


class Service_main(models.Model):
    head = models.CharField(max_length=1000, null=True, blank=True)
    text = models.CharField(max_length=2000, null=True, blank=True)
    img_back = models.ImageField(null=True, blank=True)

    def __unicode__(self):
        return '%s' % self.head

    class Meta:
        db_table = 'Service_main'
        verbose_name = 'Страничка_услуги'
        verbose_name_plural = 'Страничка_услуги'


class Price_main(models.Model):
    head = models.CharField(max_length=1000, null=True, blank=True)
    text = models.CharField(max_length=2000, null=True, blank=True)
    img_back = models.ImageField(null=True, blank=True)

    def __unicode__(self):
        return '%s' % self.head

    class Meta:
        db_table = 'Price_main'
        verbose_name = 'Страничка_цен'
        verbose_name_plural = 'Страничка_цен'


class Article_main(models.Model):
    head = models.CharField(max_length=1000, null=True, blank=True)
    text = models.CharField(max_length=2000, null=True, blank=True)
    img_back = models.ImageField(null=True, blank=True)

    def __unicode__(self):
        return '%s' % self.head

    class Meta:
        db_table = 'Article_main'
        verbose_name = 'Страничка_статей'
        verbose_name_plural = 'Страничка_статей'


class Form_cont_main(models.Model):
    form_name = models.CharField(max_length=1000, null=True, blank=True)
    head_preview = models.CharField(max_length=1000, null=True, blank=True)
    text_preview = models.CharField(max_length=2000, null=True, blank=True)
    text_ans = models.CharField(max_length=2000, null=True, blank=True)

    def __unicode__(self):
        return '%s' % self.form_name

    class Meta:
        db_table = 'Form_cont'
        verbose_name = 'Текст_формы'
        verbose_name_plural = 'Тексты_форм'


class Phone(models.Model):
    contact_key = models.ForeignKey(Contacts, null=True, blank=True)
    phone = models.CharField(max_length=200, null=True, blank=True)

    def __unicode__(self):
        return '%s' % self.phone

    class Meta:
        db_table = 'Phone'
        verbose_name = 'Телефон'
        verbose_name_plural = 'Телефоны'


class Email(models.Model):
    contact_key = models.ForeignKey(Contacts, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)

    def __unicode__(self):
        return '%s' % self.email

    class Meta:
        db_table = 'Email'
        verbose_name = 'Email'
        verbose_name_plural = 'Emails'


class Adres(models.Model):
    contact_key = models.ForeignKey(Contacts, null=True, blank=True)
    adress = models.CharField(max_length=200, null=True, blank=True)

    def __unicode__(self):
        return '%s' % self.adress

    class Meta:
        db_table = 'Adres'
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'


class Metatitle(models.Model):
    keywords = models.TextField(blank=True, default='')
    description = models.TextField(blank=True, default='')
    img = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=500, null=True, blank=True)

    def __unicode__(self):
        return '%s' % self.title

    class Meta:
        db_table = 'metatitle'