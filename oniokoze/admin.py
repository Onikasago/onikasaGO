from django.contrib import admin
from .models import Catch,Spot,LikeForPost,Fishname,Recipe
from reversion.admin import VersionAdmin

class FishnameInline(admin.StackedInline):
    model = Fishname
    extra = 3

class CatchAdmin(admin.ModelAdmin):
    inlines = [FishnameInline]


admin.site.register(Catch, CatchAdmin)
admin.site.register(Recipe)
admin.site.register(Spot)
admin.site.register(LikeForPost)

