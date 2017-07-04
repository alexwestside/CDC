# -*- coding: utf-8 -*-

from modeltranslation.translator import translator, TranslationOptions
from solar.models import *


class BannerTranslationOptions(TranslationOptions):
    fields = ('head', 'text', 'text_button')
translator.register(Banner, BannerTranslationOptions)


class AboutTranslationOptions(TranslationOptions):
    fields = ('head', 'text')
translator.register(About, AboutTranslationOptions)


class MissionTranslationOptions(TranslationOptions):
    fields = ('head', 'text')
translator.register(Mission, MissionTranslationOptions)


class CircleTranslationOptions(TranslationOptions):
    fields = ('head', 'text')
translator.register(Circle, CircleTranslationOptions)


class ProjectTranslationOptions(TranslationOptions):
    fields = ('head', 'text')
translator.register(Project, ProjectTranslationOptions)


class Category_projectTranslationOptions(TranslationOptions):
    fields = ('head', )
translator.register(Category_project, Category_projectTranslationOptions)


class PartnerTranslationOptions(TranslationOptions):
    fields = ('head', 'text')
translator.register(Partner, PartnerTranslationOptions)


class ServiceTranslationOptions(TranslationOptions):
    fields = ('head', 'text')
translator.register(Service, ServiceTranslationOptions)


class PriceTranslationOptions(TranslationOptions):
    fields = ('head', )
translator.register(Price, PriceTranslationOptions)


class Price_itemTranslationOptions(TranslationOptions):
    fields = ('power', 'price')
translator.register(Price_item, Price_itemTranslationOptions)


class ProfitTranslationOptions(TranslationOptions):
    fields = ('profit', )
translator.register(Profit, ProfitTranslationOptions)


class Price_addTranslationOptions(TranslationOptions):
    fields = ('head', 'text')
translator.register(Price_add, Price_addTranslationOptions)


class Articles_tagTranslationOptions(TranslationOptions):
    fields = ('head',)
translator.register(Articles_tag, Articles_tagTranslationOptions)


class ArticlesTranslationOptions(TranslationOptions):
    fields = ('head', 'text')
translator.register(Articles, ArticlesTranslationOptions)


class ContactsTranslationOptions(TranslationOptions):
    fields = ('head', 'text')
translator.register(Contacts, ContactsTranslationOptions)


class Project_mainTranslationOptions(TranslationOptions):
    fields = ('head', 'text')
translator.register(Project_main, Project_mainTranslationOptions)


class Service_mainTranslationOptions(TranslationOptions):
    fields = ('head', 'text')
translator.register(Service_main, Service_mainTranslationOptions)


class Price_mainTranslationOptions(TranslationOptions):
    fields = ('head', 'text')
translator.register(Price_main, Price_mainTranslationOptions)


class Form_cont_mainTranslationOptions(TranslationOptions):
    fields = ('head_preview', 'text_preview', 'text_ans')
translator.register(Form_cont_main, Form_cont_mainTranslationOptions)


class AdresTranslationOptions(TranslationOptions):
    fields = ('adress',)
translator.register(Adres, AdresTranslationOptions)


class MetatitleTranslationOptions(TranslationOptions):
    fields = ('keywords', 'description', 'title')
translator.register(Metatitle, MetatitleTranslationOptions)
