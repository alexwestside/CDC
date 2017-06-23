# -*- coding: utf-8 -*-

from modeltranslation.translator import translator, TranslationOptions
from models import *


class BannerTranslationOptions(TranslationOptions):
    fields = ('head', 'text', 'text_button')
translator.register(Banner, BannerTranslationOptions)


class AboutTranslationOptions(TranslationOptions):
    fields = ('head', 'text')
translator.register(About, AboutTranslationOptions)


class ProjectTranslationOptions(TranslationOptions):
    fields = ('head', 'text')
translator.register(Project, ProjectTranslationOptions)


class Category_projectTranslationOptions(TranslationOptions):
    fields = ('head', )
translator.register(Category_project, Category_projectTranslationOptions)
