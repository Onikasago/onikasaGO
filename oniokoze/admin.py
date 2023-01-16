from django.contrib import admin
from .models import Spot,LikeForPost
from reversion.admin import VersionAdmin

admin.site.register(Spot)
admin.site.register(LikeForPost)
