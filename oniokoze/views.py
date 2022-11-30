import logging
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
import re
from .forms import CatchCreateForm, FishnameCreateForm
from .models import Catch, Fishname
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

logger = logging.getLogger(__name__)


class IndexView(generic.TemplateView):
    template_name = "index.html"


class CatchListView(LoginRequiredMixin, generic.ListView):
    model = Fishname.objects.select_related('catch').all()
    template_name = 'catch_list.html'

    def get_queryset(self):
        catches = Catch.objects.filter(user=self.request.user).order_by('-created_at')
        return catches


class OnlyYouMixin(UserPassesTestMixin):
    raise_exception = True

    def test_func(self):
        dairy = get_object_or_404(Diary, pk=self.kwargs['pk'])
        return self.request.user == list.user


class CatchDetailView(LoginRequiredMixin, generic.DetailView):
    model = Fishname
    template_name = 'catch_detail.html'


class CatchCreateView(generic.CreateView):
    model = Fishname
    form_class = CatchCreateForm
    template_name = 'catch_create.html'
    success_url = reverse_lazy('oniokoze:catch_list')

    def form_valid(self, form):
        catch = form.save(commit=False)
        catch.user = self.request.user
        catch.save()



def get_queryset():
    catches = Fishname.objects.select_related('catch').all()
    return catches


class FishnameCreateView(generic.CreateView):
    form_class = FishnameCreateForm
    template_name = 'fishname_create.html'
    success_url = reverse_lazy('oniokoze:catch_create')

    def post(self, request, *args, **kwrgs):
          # 空の配列を作ります
        titleList= []
        bodyList= []
        noList= []
        idList= []
          # request.POST.items()でPOSTで送られてきた全てを取得。
        for i in request.POST.items():
            if re.match(r'titleList_*', i[0]):
                titleList.append(i[1])
            if re.match(r'bodyList_*', i[0]):
                bodyList.append(i[1])
            if re.match(r'noList_*', i[0]):
                noList.append(i[1])
            if re.match(r'idList_*', i[0]):
                idList.append(i[1])
        for i in range(len(titleList)):
            corporationinformation = Fishname.objects.create(
                name= titleList[i],
                size = bodyList[i],
                no = noList[i],
                catch_id= idList[i],
            )
            corporationinformation.save()
        return redirect(to='/catch-create')

class SpotListView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'spot_list.html'


class ResipeListView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'resipe_list.html'


class TriviaView(generic.TemplateView):
    template_name = 'trivia.html'


class MypageView(generic.TemplateView):
    template_name = 'mypage.html'
