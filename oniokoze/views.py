import logging
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CatchCreateForm,FishnameCreateForm
from .models import Catch, Fishname, Fish, Recipe
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
class RecipeListView(LoginRequiredMixin,generic.TemplateView):
    model = Recipe
    template_name = 'recipe_list.html'

    def recipese(request):
        recipe = Recipe.objects.order_by('-id')
        """ 検索機能の処理 """
        keyword = request.GET.get('keyword')

        if keyword:
            recipe = recipe.filter(
                Q(title__icontains=keyword)
            )
            messages.success(request, '「{}」の検索結果'.format(keyword))

        return render(request, 'oniokoze:recipe_list.html', {'recipe': recipe})

    def methodse(request):
        method = Recipe.objects.order_by('-id')
        """ 検索機能の処理 """
        keyword = request.GET.get('keyword2')

        if keyword:
            recipe = recipe.filter(
                Q(title__icontains=keyword2)
            )
            messages.success(request, '「{}」の検索結果'.format(keyword2))

        return render(request, 'oniokoze:recipe_list.html', {'recipe': recipe})






class TriviaView(generic.TemplateView):
    template_name = 'trivia.html'
class MypageView(generic.TemplateView):
    template_name = 'mypage.html'
