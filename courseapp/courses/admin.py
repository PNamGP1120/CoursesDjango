from django.contrib import admin
from .models import *
from django.utils.html import mark_safe
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class LessonForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget)
    class Meta:
        model = Lesson
        fields = '__all__'

class MyCourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'subject', 'description']
    readonly_fields = ['avatar']

    def avatar(self, obj):
        if obj:
            return mark_safe(
                '<img src = "/static/{url}" width ="120" />'\
                    .format(url=obj.image.name)
            )


class MyLessonAdmin(admin.ModelAdmin):
    form = LessonForm
    list_display = ['id', 'subject', 'active', 'created_date']
    search_fields = ['subject']
    list_filter = ['id', 'created_date']
    list_editable = ['subject', 'active']
    # readonly_fields = ['image_view']
    #
    # # def image_view(self, obj):
    # #     return f'<img src="/static/{obj.image.url}" />'

    class Media:
        css = {
            'all': ('/static/css/styles.css',)
        }
        js = ('/static/js/scripts.js',)

admin.site.register(Lesson, MyLessonAdmin)
admin.site.register(Course, MyCourseAdmin)
admin.site.register(Tag)

