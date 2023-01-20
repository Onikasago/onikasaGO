import logging
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CatchCreateForm,FishnameCreateForm,RecipeCreateForm
from .models import Catch,Fishname,Fish,Recipe
from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, get_object_or_404



logger = logging.getLogger(__name__)

class IndexView(generic.TemplateView):
    template_name = "index.html"


class CatchListView(LoginRequiredMixin, generic.ListView):
    model = Catch
    template_name = 'catch_list.html'

    def get_queryset(self):
        catches = Catch.objects.filter(user=self.request.user).order_by('-created_at')
        return catches




class CatchCreateView(generic.CreateView):
    model = Catch
    form_class = CatchCreateForm
    template_name = 'catch_create.html'
    success_url = reverse_lazy('oniokoze:catch-list')

class FishnameCreateView(generic.CreateView):
    model = Fishname
    form_class = FishnameCreateForm
    template_name = 'fishname_create.html'
    success_url = reverse_lazy('oniokoze:catch-create')

class SpotListView(LoginRequiredMixin,generic.TemplateView):
    template_name = 'spot_list.html'
class RecipeListView(LoginRequiredMixin,generic.ListView):
    model = Recipe
    template_name = 'recipe_list.html'
    paginate_by = 3

    def get_queryset(self, **kwargs):
        queryset = super().get_queryset(**kwargs)
        query = self.request.GET

        if q := query.get('q') : # python3.8以降
            if p := query.get('p'):
                if p == '#':
                    queryset = queryset.filter( Q(method__icontains=q) )
                elif q == '#':
                    queryset = queryset.filter( Q(title__icontains=p) )
                else:
                    queryset = queryset.filter( Q(method__icontains=q) & Q(title__icontains=p))

        return queryset.order_by('-created_at')



class RecipeCreateView(generic.CreateView):
    model = Recipe
    form_class = RecipeCreateForm
    template_name = 'recipe_create.html'
    success_url = reverse_lazy('oniokoze:recipe-create')


class TriviaView(generic.TemplateView):
    template_name = 'trivia.html'
class MypageView(generic.TemplateView):
    template_name = 'mypage.html'
