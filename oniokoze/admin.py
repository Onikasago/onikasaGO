from django.contrib import admin
from .models import Spot
from reversion.admin import VersionAdmin

admin.site.register(Spot)
