import logging
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from.models import Catch
from django.shortcuts import get_object_or_404

logger = logging.getLogger(__name__)

class IndexView(generic.TemplateView):
    template_name = "index.html"