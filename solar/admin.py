# -*- coding: utf-8 -*-
from django.contrib import admin

# Register your models here.

from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from modeltranslation.admin import TabbedTranslationAdmin
from solar.models import *
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from import_export import fields
from import_export.widgets import ForeignKeyWidget
from django_summernote.admin import SummernoteModelAdmin, SummernoteWidget

# Register your models here.


class BannerResource(resources.ModelResource):
    class Meta:
        model = Banner
        fields = [field.name for field in Banner._meta.fields]
        import_id_fields = [
            'id', ]  # it means that the instance could be updated if the instance with the value in this filed exists


class BannerAdmin(ImportExportModelAdmin, SummernoteModelAdmin):
    resource_class = BannerResource
    list_display = [field.name for field in Banner._meta.fields]
    search_fields = [field.name for field in Banner._meta.fields]
    list_filter = [field.name for field in Banner._meta.fields]

admin.site.register(Banner, BannerAdmin)


class Project_mainResource(resources.ModelResource):
    class Meta:
        model = Project_main
        fields = [field.name for field in Project_main._meta.fields]
        import_id_fields = [
            'id', ]  # it means that the instance could be updated if the instance with the value in this filed exists


class Project_mainAdmin(ImportExportModelAdmin, SummernoteModelAdmin):
    resource_class = Project_mainResource
    list_display = [field.name for field in Project_main._meta.fields]
    search_fields = [field.name for field in Project_main._meta.fields]
    list_filter = [field.name for field in Project_main._meta.fields]


admin.site.register(Project_main, Project_mainAdmin)


class Form_cont_mainResource(resources.ModelResource):
    class Meta:
        model = Form_cont_main
        fields = [field.name for field in Form_cont_main._meta.fields]
        import_id_fields = [
            'id', ]  # it means that the instance could be updated if the instance with the value in this filed exists


class Form_cont_mainAdmin(ImportExportModelAdmin, SummernoteModelAdmin):
    resource_class = Form_cont_mainResource
    list_display = [field.name for field in Form_cont_main._meta.fields]
    search_fields = [field.name for field in Form_cont_main._meta.fields]
    list_filter = [field.name for field in Form_cont_main._meta.fields]


admin.site.register(Form_cont_main, Form_cont_mainAdmin)


class Service_mainResource(resources.ModelResource):
    class Meta:
        model = Service_main
        fields = [field.name for field in Service_main._meta.fields]
        import_id_fields = [
            'id', ]  # it means that the instance could be updated if the instance with the value in this filed exists


class Service_mainAdmin(ImportExportModelAdmin, SummernoteModelAdmin):
    resource_class = Service_mainResource
    list_display = [field.name for field in Service_main._meta.fields]
    search_fields = [field.name for field in Service_main._meta.fields]
    list_filter = [field.name for field in Service_main._meta.fields]


admin.site.register(Service_main, Service_mainAdmin)


class Price_mainResource(resources.ModelResource):
    class Meta:
        model = Price_main
        fields = [field.name for field in Price_main._meta.fields]
        import_id_fields = [
            'id', ]  # it means that the instance could be updated if the instance with the value in this filed exists


class Price_mainAdmin(ImportExportModelAdmin, SummernoteModelAdmin):
    resource_class = Price_mainResource
    list_display = [field.name for field in Price_main._meta.fields]
    search_fields = [field.name for field in Price_main._meta.fields]
    list_filter = [field.name for field in Price_main._meta.fields]


admin.site.register(Price_main, Price_mainAdmin)


class Article_mainResource(resources.ModelResource):
    class Meta:
        model = Article_main
        fields = [field.name for field in Article_main._meta.fields]
        import_id_fields = [
            'id', ]  # it means that the instance could be updated if the instance with the value in this filed exists


class Article_mainAdmin(ImportExportModelAdmin, SummernoteModelAdmin):
    resource_class = Article_mainResource
    list_display = [field.name for field in Article_main._meta.fields]
    search_fields = [field.name for field in Article_main._meta.fields]
    list_filter = [field.name for field in Article_main._meta.fields]


admin.site.register(Article_main, Article_mainAdmin)



class AboutResource(resources.ModelResource):
    class Meta:
        model = About
        fields = [field.name for field in About._meta.fields]
        import_id_fields = [
            'id', ]  # it means that the instance could be updated if the instance with the value in this filed exists


class AboutAdmin(ImportExportModelAdmin, SummernoteModelAdmin):
    resource_class = AboutResource
    list_display = [field.name for field in About._meta.fields]
    search_fields = [field.name for field in About._meta.fields]
    list_filter = [field.name for field in About._meta.fields]

admin.site.register(About, AboutAdmin)


class MissionResource(resources.ModelResource):
    class Meta:
        model = Mission
        fields = [field.name for field in Mission._meta.fields]
        import_id_fields = [
            'id', ]  # it means that the instance could be updated if the instance with the value in this filed exists


class MissionAdmin(ImportExportModelAdmin, SummernoteModelAdmin):
    resource_class = MissionResource
    list_display = [field.name for field in Mission._meta.fields]
    search_fields = [field.name for field in Mission._meta.fields]
    list_filter = [field.name for field in Mission._meta.fields]

admin.site.register(Mission, MissionAdmin)


class CircleResource(resources.ModelResource):
    class Meta:
        model = Circle
        fields = [field.name for field in Circle._meta.fields]
        import_id_fields = [
            'id', ]  # it means that the instance could be updated if the instance with the value in this filed exists


class CircleAdmin(ImportExportModelAdmin, SummernoteModelAdmin):
    resource_class = CircleResource
    list_display = [field.name for field in Circle._meta.fields]
    search_fields = [field.name for field in Circle._meta.fields]
    list_filter = [field.name for field in Circle._meta.fields]
    
admin.site.register(Circle, CircleAdmin)


class ProjectResource(resources.ModelResource):
    class Meta:
        model = Project
        fields = [field.name for field in Project._meta.fields]
        import_id_fields = [
            'id', ]  # it means that the instance could be updated if the instance with the value in this filed exists


class ImgInline(admin.TabularInline):
    model = Img_project


class ProjectAdmin(ImportExportModelAdmin, SummernoteModelAdmin):
    resource_class = ProjectResource
    list_display = [field.name for field in Project._meta.fields]
    search_fields = [field.name for field in Project._meta.fields]
    list_filter = [field.name for field in Project._meta.fields]
    inlines = [ImgInline]

admin.site.register(Project, ProjectAdmin)


class Category_projectResource(resources.ModelResource):
    class Meta:
        model = Category_project
        fields = [field.name for field in Category_project._meta.fields]
        import_id_fields = [
            'id', ]  # it means that the instance could be updated if the instance with the value in this filed exists


class Category_projectAdmin(ImportExportModelAdmin, SummernoteModelAdmin):
    resource_class = Category_projectResource
    list_display = [field.name for field in Category_project._meta.fields]
    search_fields = [field.name for field in Category_project._meta.fields]
    list_filter = [field.name for field in Category_project._meta.fields]


admin.site.register(Category_project, Category_projectAdmin)


class PartnerResource(resources.ModelResource):
    class Meta:
        model = Partner
        fields = [field.name for field in Partner._meta.fields]
        import_id_fields = [
            'id', ]  # it means that the instance could be updated if the instance with the value in this filed exists


class PartnerAdmin(ImportExportModelAdmin, SummernoteModelAdmin):
    resource_class = PartnerResource
    list_display = [field.name for field in Partner._meta.fields]
    search_fields = [field.name for field in Partner._meta.fields]
    list_filter = [field.name for field in Partner._meta.fields]


admin.site.register(Partner, PartnerAdmin)


class ServiceResource(resources.ModelResource):
    class Meta:
        model = Service
        fields = [field.name for field in Service._meta.fields]
        import_id_fields = [
            'id', ]  # it means that the instance could be updated if the instance with the value in this filed exists


class Img_service_Inline(admin.TabularInline):
    model = Img_Service


class ServiceAdmin(ImportExportModelAdmin, SummernoteModelAdmin):
    resource_class = ServiceResource
    list_display = [field.name for field in Service._meta.fields]
    search_fields = [field.name for field in Service._meta.fields]
    list_filter = [field.name for field in Service._meta.fields]
    inlines = [Img_service_Inline]

admin.site.register(Service, ServiceAdmin)


class PriceResource(resources.ModelResource):
    class Meta:
        model = Price
        fields = [field.name for field in Price._meta.fields]
        import_id_fields = [
            'id', ]  # it means that the instance could be updated if the instance with the value in this filed exists


class Price_Inline(admin.TabularInline):
    model = Price_item


class Profit_Inline(admin.TabularInline):
    model = Profit


class PriceAdmin(ImportExportModelAdmin, SummernoteModelAdmin):
    resource_class = PriceResource
    list_display = [field.name for field in Price._meta.fields]
    search_fields = [field.name for field in Price._meta.fields]
    list_filter = [field.name for field in Price._meta.fields]
    inlines = [Price_Inline, Profit_Inline]

admin.site.register(Price, PriceAdmin)


class Price_addResource(resources.ModelResource):
    class Meta:
        model = Price_add
        fields = [field.name for field in Price_add._meta.fields]
        import_id_fields = [
            'id', ]  # it means that the instance could be updated if the instance with the value in this filed exists


class Price_addAdmin(ImportExportModelAdmin, SummernoteModelAdmin):
    resource_class = Price_addResource
    list_display = [field.name for field in Price_add._meta.fields]
    search_fields = [field.name for field in Price_add._meta.fields]
    list_filter = [field.name for field in Price_add._meta.fields]

admin.site.register(Price_add, Price_addAdmin)


class Articles_tagResource(resources.ModelResource):
    class Meta:
        model = Articles_tag
        fields = [field.name for field in Articles_tag._meta.fields]
        import_id_fields = [
            'id', ]  # it means that the instance could be updated if the instance with the value in this filed exists


class Articles_tagAdmin(ImportExportModelAdmin, SummernoteModelAdmin):
    resource_class = Articles_tagResource
    list_display = [field.name for field in Articles_tag._meta.fields]
    search_fields = [field.name for field in Articles_tag._meta.fields]
    list_filter = [field.name for field in Articles_tag._meta.fields]

admin.site.register(Articles_tag, Articles_tagAdmin)


class ArticlesResource(resources.ModelResource):
    class Meta:
        model = Articles
        fields = [field.name for field in Articles._meta.fields]
        import_id_fields = [
            'id', ]  # it means that the instance could be updated if the instance with the value in this filed exists


class ArticlesAdmin(ImportExportModelAdmin, SummernoteModelAdmin):
    resource_class = ArticlesResource
    list_display = [field.name for field in Articles._meta.fields]
    search_fields = [field.name for field in Articles._meta.fields]
    list_filter = [field.name for field in Articles._meta.fields]

admin.site.register(Articles, ArticlesAdmin)


class ContactsResource(resources.ModelResource):
    class Meta:
        model = Contacts
        fields = [field.name for field in Contacts._meta.fields]
        import_id_fields = [
            'id', ]  # it means that the instance could be updated if the instance with the value in this filed exists


class AdresInline(admin.TabularInline):
    model = Adres


class PhoneInline(admin.TabularInline):
    model = Phone


class EmailInline(admin.TabularInline):
    model = Email


class ContactsAdmin(ImportExportModelAdmin, SummernoteModelAdmin):
    resource_class = ContactsResource
    list_display = [field.name for field in Contacts._meta.fields]
    search_fields = [field.name for field in Contacts._meta.fields]
    list_filter = [field.name for field in Contacts._meta.fields]
    inlines = [AdresInline, PhoneInline, EmailInline]
admin.site.register(Contacts, ContactsAdmin)


class MetatitleResource(resources.ModelResource):
    class Meta:
        model = Metatitle
        fields = [field.name for field in Metatitle._meta.fields]
        import_id_fields = [
            'id', ]  # it means that the instance could be updated if the instance with the value in this filed exists


class MetatitleAdmin(ImportExportModelAdmin):
    resource_class = MetatitleResource
    list_display = [field.name for field in Metatitle._meta.fields]
    search_fields = [field.name for field in Metatitle._meta.fields]
    list_filter = [field.name for field in Metatitle._meta.fields]

admin.site.register(Metatitle, MetatitleAdmin)

