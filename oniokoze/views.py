import logging
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CatchCreateForm,FishnameCreateForm
from .models import Catch,Fishname
from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect


logger = logging.getLogger(__name__)

class IndexView(generic.TemplateView):
    template_name = "index.html"


class CatchListView(LoginRequiredMixin, generic.ListView):
    model = Catch
    template_name = 'catch_list.html'

    def get_queryset(self):
        catches = Catch.objects.filter(user=self.request.user).order_by('-created_at')
        return catches


class CatchCreateView( generic.CreateView):
    model = Catch
    form_class = CatchCreateForm
    template_name = 'catch_create.html'
    success_url = reverse_lazy('oniokoze:catch-list')

class FishnameCreateView(generic.CreateView):
    model = Fishname
    form_class = FishnameCreateForm
    template_name = 'fishname_create.html'
    success_url = reverse_lazy('oniokoze:catch-create')







