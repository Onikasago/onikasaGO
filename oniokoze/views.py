import logging
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import CatchCreateForm, FishnameCreateForm,SpotCreateForm
from .models import Catch, Fishname,Spot, LikeForPost
from django.shortcuts import render, redirect ,get_object_or_404
from django.contrib import messages
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect,JsonResponse
from django.db.models import Q

logger = logging.getLogger(__name__)


def spot(request):
    spot = Spot.objects.order_by('-id')
    """ 検索機能の処理 """
    keyword = request.GET.get('keyword')

    if keyword:
        """ テキスト用のQオブジェクトを追加 """
        spot = spot.filter(
            Q(place__icontains=keyword) | Q(capitl__icontains=keyword)
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
        oniokoze = get_object_or_404(Spot,pk=self.kwargs['pk'])
        return self.request.user == oniokoze.user


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
                            Q(place__icontains=keyword) | Q(capital__icontains=keyword)
                       )
            messages.success(self.request, '「{}」の検索結果'.format(keyword))

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # {'pk':{'count':ポストに対するイイネ数,'is_user_liked_for_post':bool},}という辞書を追加していく
        d = {}
        for spot in self.object_list:
            # postに対するイイね数
            like_for_post_count = spot.likeforpost_set.count()
            # ログイン中のユーザーがイイねしているかどうか
            is_user_liked_for_post = False
            if not self.request.user.is_anonymous:
                if spot.likeforpost_set.filter(user=self.request.user).exists():
                    is_user_liked_for_post = True

            d[spot.pk] = {'count': like_for_post_count, 'is_user_liked_for_post': is_user_liked_for_post}
        context['post_like_data'] = d
        return context

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

class SpotDetailView(LoginRequiredMixin,generic.DetailView):
    model = Spot
    template_name = 'spot_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        like_for_post_count = self.object.likeforpost_set.count()
        # ポストに対するイイね数
        context['like_for_post_count'] = like_for_post_count
        # ログイン中のユーザーがイイねしているかどうか
        is_user_liked_for_post = False
        if not self.request.user.is_anonymous:
            if self.object.likeforpost_set.filter(user=self.request.user).exists():
                is_user_liked_for_post = True
        context['is_user_liked_for_post'] = is_user_liked_for_post

        return context

def like_for_post(request):
    spot_pk = request.POST.get('spot_pk')
    context = {
        'user': f'{request.user.last_name} {request.user.first_name}',
    }
    spotpost = get_object_or_404(Spot, pk=spot_pk)
    like = LikeForPost.objects.filter(target=spotpost, user=request.user)
    if like.exists():
        like.delete()
        context['method'] = 'delete'
    else:
        like.create(target=spotpost, user=request.user)
        context['method'] = 'create'

    context['like_for_post_count'] = spotpost.likeforpost_set.count()

    return JsonResponse(context)

class SpotUpdateView(LoginRequiredMixin,OnlyYouMixin,generic.UpdateView):
    model = Spot
    template_name = 'spot_update.html'
    form_class = SpotCreateForm

    def get_success_url(self):
        return reverse_lazy('oniokoze:spot_detail',kwargs={'pk':self.kwargs['pk']})

    def form_valid(self,form):
        messages.success(self.request,'日記を更新しました。')
        return super().form_valid(form)
    def form_invalid(self,form):
        messages.error(self.request,"日記の更新に失敗しました。")
        return super().form_invalid(form)

class SpotDeleteView(LoginRequiredMixin,OnlyYouMixin,generic.DeleteView):
    model = Spot
    template_name = 'spot_delete.html'
    success_url = reverse_lazy('oniokoze:spot_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request,"日記を削除しました。")
        return super().delete(request,*args,**kwargs)

