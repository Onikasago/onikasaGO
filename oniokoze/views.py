import logging
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
import re
from .forms import CatchCreateForm, FishnameCreateForm,SpotCreateForm
from .models import Catch, Fishname,Spot
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.db.models import Q

logger = logging.getLogger(__name__)


def spot(request):
    spot = Spot.objects.order_by('-id')
    """ 検索機能の処理 """
    keyword = request.GET.get('keyword')

    if keyword:
        """ テキスト用のQオブジェクトを追加 """
        spot = spot.filter(
            Q(title__icontains=keyword) | Q(text__icontains=keyword)
        )
        messages.success(request, '「{}」の検索結果'.format(keyword))

    return render(request, 'oniokoze/spot_list.html', {'spot': spot})

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

class SpotListView(LoginRequiredMixin,generic.ListView):
    model = Spot
    template_name = 'spot_list.html'


    def get_queryset(self):
        spots = Spot.objects.filter(user=self.request.user).order_by('-created_at')
        return spots

    def get_queryset(self):
        queryset = Spot.objects.order_by('-id')
        keyword = self.request.GET.get('keyword')

        if keyword:
            queryset = queryset.filter(
                            Q(title__icontains=keyword) | Q(text__icontains=keyword)
                       )
            messages.success(self.request, '「{}」の検索結果'.format(keyword))

        return queryset


class ResipeListView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'resipe_list.html'


class TriviaView(generic.TemplateView):
    template_name = 'trivia.html'


class MypageView(generic.TemplateView):
    template_name = 'mypage.html'

class SpotCreateView(LoginRequiredMixin,generic.CreateView):
    model = Spot
    template_name = 'spot_create.html'
    form_class=SpotCreateForm
    success_url=reverse_lazy('oniokoze:spot_list')

    def form_valid(self,form):
        spot=form.save(commit=False)
        spot.user=self.request.user
        spot.save()
        messages.success(self.request,'日記を作成しました。')
        return super().form_valid(form)
    def form_invalid(self,form):
        messages.error(self.request,"日記の作成に失敗しました。")
        return super().form_invalid(form)