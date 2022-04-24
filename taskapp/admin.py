from django.contrib import admin
from .models import Content, Rate
# Register your models here.

class ContentAdmin(admin.ModelAdmin):
    list_display        = ['id', 'title', 'average_score', 'number_of_users_rated']
    list_display_links  = ['title', 'average_score', 'number_of_users_rated']

class RateAdmin(admin.ModelAdmin):
    list_display       = ['content', 'user', 'score']
    list_display_links = ['content', 'user', 'score']


admin.site.register(Content, ContentAdmin)
admin.site.register(Rate, RateAdmin)