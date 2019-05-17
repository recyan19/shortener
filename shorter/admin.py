from django.contrib import admin

from shorter.models import Url


class UrlAdmin(admin.ModelAdmin):
    list_display = ('url_id', 'url', 'pub_date', 'count')
    ordering = ('-pub_date',)


admin.site.register(Url, UrlAdmin)
