from django.contrib import admin

from .models import *


class FishnameInline(admin.StackedInline):
    model = Fishname
    extra = 3


class CatchAdmin(admin.ModelAdmin):
    inlines = [FishnameInline]


admin.site.register(Catch, CatchAdmin)