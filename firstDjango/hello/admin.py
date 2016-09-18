from django.contrib import admin
from hello.models import *
# Register your models here.

admin.site.register(Author)
admin.site.register(AuthorDetail)
admin.site.register(Book)

@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name','country','state_province','city')
    search_fields = ('name','city')
    list_filter = ('state_province',)
    # ordering = ('id',)
    # fields = ('name','state_province')
    # exclude = ('name', 'state_province')
    fieldsets = (
            (None, {
                'fields': ('url', 'title', 'content', 'sites')
            }),
            ('Advanced options', {
                'classes': ('collapse',),
                'fields': ('registration_required', 'template_name'),
            }),
    )

# admin.site.register(Publisher,PublisherAdmin)

