from django.contrib import admin

# Register your models here.

from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from modeltranslation.admin import TabbedTranslationAdmin
from models import *
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
