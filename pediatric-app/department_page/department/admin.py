from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from .models import *


class AdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = General
        fields = '__all__'


class GeneralAdmin(admin.ModelAdmin):
    form = AdminForm
    list_display = ('title', 'address', 'phone', 'photo')
    list_display_links = ('title',)


class NewsAdmin(admin.ModelAdmin):
    form = AdminForm
    prepopulated_fields = {"slug": ('title',)}
    list_display = ('id', 'title', 'time_created', 'photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_created')


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('name',)}
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


admin.site.register(General, GeneralAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Sotr)
admin.site.register(Articles)