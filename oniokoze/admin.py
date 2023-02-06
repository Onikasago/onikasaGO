from django.contrib import admin
from .models import Catch,Spot,Fishname,Recipe,Order,Fish,LikeForSpot,LikeForCatch,LikeForRecipe
from reversion.admin import VersionAdmin

class FishnameInline(admin.StackedInline):
    model = Fishname
    extra = 3

class CatchAdmin(admin.ModelAdmin):
    inlines = [FishnameInline]


admin.site.register(Catch)
admin.site.register(Fishname)
admin.site.register(Recipe)
admin.site.register(Order)
admin.site.register(Spot)
admin.site.register(Fish)
admin.site.register(LikeForSpot)
admin.site.register(LikeForCatch)
admin.site.register(LikeForRecipe)

