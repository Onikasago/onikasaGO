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
        catches = Catch.objects.order_by('-created_at')  #.filter(user=self.request.user)
        return catches




class CatchCreateView(generic.CreateView):
    model = Catch
    form_class = CatchCreateForm
    template_name = 'catch_create.html'
    success_url = reverse_lazy('oniokoze:catch-list')


class SpotListView(LoginRequiredMixin,generic.TemplateView):
    template_name = 'spot_list.html'
class RecipeListView(LoginRequiredMixin,generic.ListView):
    model = Recipe
    template_name = 'recipe_list.html'
    paginate_by = 3


    def get_queryset(self, **kwargs):
        queryset = super().get_queryset(**kwargs)
        query = self.request.GET
        list = [0,0]

        if q := query.get('q') : # python3.8以降
            list[0]=1

            if p := query.get('p'):
                list[1]=2

            if (list[0] == 1) and (list[1] == 2):
                    queryset = queryset.filter(Q(method__icontains=q) & Q(title__icontains=p))

            elif (list[0] == 1) and (list[1] != 2):
                    queryset = queryset.filter(Q(method__icontains=q))

            elif (list[0] != 1) and (list[1] == 2):
                    queryset = queryset.filter(Q(title__icontains=p))

        return queryset.order_by('-created_at')




class RecipeCreateView(generic.CreateView):
    model = Recipe
    form_class = RecipeCreateForm
    template_name = 'recipe_create.html'
    success_url = reverse_lazy('oniokoze:recipe_list')

class RecipeDetailView(generic.DetailView):
    model = Recipe
    template_name = 'recipe_detail.html'

class RecipeDeleteView(generic.DeleteView):
    model = Recipe
    template_name = 'recipe_delete.html'
    success_url = reverse_lazy('oniokoze:recipe_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "日記を削除しました。")
        return super().delete(request, *args, **kwargs)


class RecipeUpdateView(generic.UpdateView):
    model = Recipe
    template_name = 'recipe_update.html'
    form_class = RecipeCreateForm

    def get_success_url(self):
        return reverse_lazy('oniokoze:recipe_detail', kwargs = {'pk':self.kwargs['pk']})

    def form_valid(self, form):
        messages.success(self.request, '日記を更新しました。')
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.error(self.request, "日記の更新に失敗しました。")
        return super().form_invalid(form)


class TriviaView(generic.TemplateView):
    template_name = 'trivia.html'
class MypageView(generic.TemplateView):
    template_name = 'mypage.html'
