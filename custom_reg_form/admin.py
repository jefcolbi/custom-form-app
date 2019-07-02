from django.contrib import admin
from .models import ExtraInfo

class ExtraInfoAdmin(admin.ModelAdmin):
    list_display = ('user', 'number')

admin.site.register(ExtraInfo)
