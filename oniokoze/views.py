import logging
import re
from django.views import generic,View
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .forms import *
from .models import *
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect,JsonResponse
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from . import forms
from accounts.models import CustomUser



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

class OnlyYouMixin(UserPassesTestMixin):
    raise_exception = True

    def test_func(self):
        oniokoze = get_object_or_404(Spot,pk=self.kwargs['pk'])
        return self.request.user == oniokoze.user
class FuckYouMixin(UserPassesTestMixin):
    raise_exception = True

    def test_func(self):
        recipe = get_object_or_404(Recipe, pk=self.kwargs['pk'])
        return self.request.user == recipe.user

class GotoHellMixin(UserPassesTestMixin):
    raise_exception = True

    def test_func(self):
        user = get_object_or_404(CustomUser,pk=self.kwargs['pk'])
        return self.request.user.id == user.id


class IndexView(generic.TemplateView):
    template_name = "index.html"



class CatchListView(LoginRequiredMixin, generic.ListView):
    model = Catch
    template_name = 'catch_list.html'
    paginate_by = 3
    def get_queryset(self, **kwargs):
        queryset = super().get_queryset(**kwargs)
        query = self.request.GET
        list = [0]

        if p := query.get('p'):
            if p == '':
                list[0] = 9
            else:
                list[0] = 1

                if list[0] == 1:
                    queryset = queryset.filter(Q(nametitle__icontains=p)| Q(place__icontains=p))
                elif list[0] == 9:
                    queryset = 'ヒットしませんでした/nワードを変えてお試しください'

        return queryset.order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # {'pk':{'count':ポストに対するイイネ数,'is_user_liked_for_post':bool},}という辞書を追加していく
        d = {}
        for catch in self.object_list:
            # postに対するイイね数
            like_for_catch_count = catch.likeforcatch_set.count()
            # ログイン中のユーザーがイイねしているかどうか
            is_user_liked_for_catch = False
            if not self.request.user.is_anonymous:
                if catch.likeforcatch_set.filter(user=self.request.user).exists():
                    is_user_liked_for_catch = True

            d[catch.pk] = {'count': like_for_catch_count, 'is_user_liked_for_catch': is_user_liked_for_catch}
        context['catch_like_data'] = d
        return context

class CatchCreateView(LoginRequiredMixin,generic.CreateView):
    model = Catch
    form_class = CatchCreateForm
    template_name = 'catch_create.html'
    success_url = reverse_lazy('oniokoze:fishname_create')
    def form_valid(self, form):
        catch = form.save(commit=False)
        catch.user = self.request.user
        catch.save()
        messages.success(self.request, '項目を作成しました。')
        return super().form_valid(form)
def catch_create(request):
    form = CatchCreateForm(request.POST or None)
    context = {'form':form}

    if request.method == "post":
        post = form.save(commit=False)
        formset = CatchFormset(request.POST,instance=post)
        if formset.is_valid():
            post.save()
            formset.save()
            return redirect('oniokoze:catch_create')
    else:
        context['formset'] = CatchFormset()
        print('SYSTEM ERROR')

    return render(request, 'catch_create.html' , context)


class CatchDetailView(LoginRequiredMixin, generic.DetailView):
    model = Fishname
    model = Catch

    slug_field = "catch_id"
    slug_url_kwarg = "catch_id"
    template_name = 'catch_detail.html'



    def add_parm(self,request):
        id = self.request.GET.get()
        context = Fishname.objects.filter(catch_id='id')
        return render(request,'catch_detail.html',context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        like_for_catch_count = self.object.likeforcatch_set.count()
         # ポストに対するイイね数
        context['like_for_catch_count'] = like_for_catch_count
         # ログイン中のユーザーがイイねしているかどうか
        is_user_liked_for_catch = False
        if not self.request.user.is_anonymous:
            if self.object.likeforcatch_set.filter(user=self.request.user).exists():
                is_user_liked_for_catch = True
        context['is_user_liked_for_catch'] = is_user_liked_for_catch
        return context


def like_for_catch(request):
    catch_pk = request.POST.get('catch_pk')
    context = {
        'user': f'{request.user.last_name} {request.user.first_name}',
    }
    catchpost = get_object_or_404(Catch, pk=catch_pk)
    like = LikeForCatch.objects.filter(target=catchpost, user=request.user)
    if like.exists():
        like.delete()
        context['method'] = 'delete'
    else:
        like.create(target=catchpost, user=request.user)
        context['method'] = 'create'

    context['like_for_catch_count'] = catchpost.likeforcatch_set.count()

    return JsonResponse(context)

class CatchUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Catch
    template_name = 'catch_update.html'
    form_class = CatchCreateForm

    def get_success_url(self):
        return reverse_lazy('oniokoze:catch_detail',kwargs={'pk':self.kwargs['pk']})

    def form_valid(self, form):
        messages.success(self.request,'項目を更新しました')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request,'項目の更新に失敗しました')
        return super().form_invalid(form)

class CatchDeleteView(LoginRequiredMixin,generic.DeleteView):
    model = Catch
    template_name = 'catch_delete.html'
    success_url = reverse_lazy('oniokoze:catch_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request,"項目を削除しました")
        return super().delete(request,*args, **kwargs)
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
        n=1
          # request.POST.items()でPOSTで送られてきた全てを取得。
        for i in request.POST.items():
            if re.match(r'titleList_*', i[0]):
                titleList.append(i[1])
            if re.match(r'bodyList_*', i[0]):
                bodyList.append(i[1])

            noList.append(n)
            n+=1

        for i in range(len(titleList)):
            corporationinformation = Fishname.objects.create(
                name= titleList[i],
                size = bodyList[i],
                no = noList[i],
                catch_id= Catch.objects.order_by('created_at').last().pk
            )
            corporationinformation.save()
        return redirect(to='/catch-list')

class FishnameUpdateView(generic.UpdateView):
    template_name = 'fishname_update.html'
    model = Fishname
    form_class = FishnameCreateForm

    def get_success_url(self):
        id = Fishname.catch
        # return reverse_lazy('oniokoze:catch_detail',kwargs={'pk':self.kwargs['pk']})
        return reverse_lazy('oniokoze:catch_detail')

    def form_valid(self, form):
        messages.success(self.request, '項目を更新しました')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, '項目の更新に失敗しました')
        return super().form_invalid(form)

class SpotListView(LoginRequiredMixin,generic.ListView):
    model = Spot
    template_name = 'spot_list.html'

    def get_queryset(self, **kwargs):
        queryset = super().get_queryset(**kwargs)
        query = self.request.GET
        list = [0, 0]

        if k := query.get('keyword'):  # python3.8以降
            if k == '':
                list[0] = 0
            else:
                list[0] = 1

        if b := query.get('beginner'):
            if b == '':
                list[1] = 9
                b = False

            elif b == 'on':
                list[1] = 2
                b = True

        if (list[0] == 1) and (list[1] == 2):
            queryset = queryset.filter(Q(place__icontains=k) & Q(beginner__icontains=b))

        elif (list[0] == 1) and (list[1] != 2):
            queryset = queryset.filter(Q(place__icontains=k))

        elif (list[0] != 1) and (list[1] == 2):
            queryset = queryset.filter(Q(beginner__icontains=b))

        elif (list[0] == 0) and (list[1] == 2):
            queryset = queryset.filter(Q(beginner__icontains=b))

        return queryset.order_by('-created_at')

    # def get_queryset(self):
    #     queryset = Spot.objects.order_by('-id')
    #     keyword = self.request.GET.get('keyword')
    #
    #     if keyword:
    #         queryset = queryset.filter(
    #                         Q(place__icontains=keyword) | Q(capital__icontains=keyword)
    #                    )
    #         messages.success(self.request, '「{}」の検索結果'.format(keyword))
    #
    #     return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # {'pk':{'count':ポストに対するイイネ数,'is_user_liked_for_post':bool},}という辞書を追加していく
        d = {}
        for spot in self.object_list:
            # postに対するイイね数
            like_for_spot_count = spot.likeforspot_set.count()
            # ログイン中のユーザーがイイねしているかどうか
            is_user_liked_for_spot = False
            if not self.request.user.is_anonymous:
                if spot.likeforspot_set.filter(user=self.request.user).exists():
                    is_user_liked_for_spot = True

            d[spot.pk] = {'count': like_for_spot_count, 'is_user_liked_for_spot': is_user_liked_for_spot}
        context['spot_like_data'] = d
        return context

class SpotCreateView(LoginRequiredMixin,generic.CreateView):
    model = Spot
    template_name = 'spot_create.html'
    form_class=SpotCreateForm
    success_url=reverse_lazy('oniokoze:fish_create')

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
        like_for_spot_count = self.object.likeforspot_set.count()
        # ポストに対するイイね数
        context['like_for_spot_count'] = like_for_spot_count
        # ログイン中のユーザーがイイねしているかどうか
        is_user_liked_for_spot = False
        if not self.request.user.is_anonymous:
            if self.object.likeforspot_set.filter(user=self.request.user).exists():
                is_user_liked_for_spot = True
        context['is_user_liked_for_spot'] = is_user_liked_for_spot

        return context

def like_for_spot(request):
    spot_pk = request.POST.get('spot_pk')
    context = {
        'user': f'{request.user.last_name} {request.user.first_name}',
    }
    spotpost = get_object_or_404(Spot, pk=spot_pk)
    like = LikeForSpot.objects.filter(target=spotpost, user=request.user)
    if like.exists():
        like.delete()
        context['method'] = 'delete'
    else:
        like.create(target=spotpost, user=request.user)
        context['method'] = 'create'

    context['like_for_spot_count'] = spotpost.likeforspot_set.count()

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

def getPrefecture(request):
    prefecture = request.POST.get('prefecture')
    prefecutres = return_cities_by_prefecture(prefecture)
    return JsonResponse({'prefecutres': prefecutres})

def processForm(request):
    context = {}
    if request.method == 'GET':
        form = AddressForm()
        context['form'] = form
        return render(request, 'spot_list.html', context)

    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            selected_province = request.POST['city']
            obj = form.save(commit=False)
            obj.state = selected_province
            obj.save()

class OrderCreateView(generic.CreateView):
    form_class = OrderCreateForm
    template_name = 'order_create.html'
    success_url = reverse_lazy('oniokoze:recipe_create')

    def post(self, request, *args, **kwrgs):
          # 空の配列を作ります
        orderList= []
        procedureList= []
        materialList= []
        amountList = []
        unitList = []
        n=0
          # request.POST.items()でPOSTで送られてきた全てを取得。
        for i in request.POST.items():

            if re.match(r'procedureList_*', i[0]):
                procedureList.append(i[1])
            if re.match(r'photoList_*', i[0]):
                photoList.append(i[1])
            if re.match(r'materialList_*', i[0]):
                materialList.append(i[1])
            if re.match(r'amountList_*', i[0]):
                if (i[1]==''):
                    amountList.append(0)
                else:
                    amountList.append(i[1])
            if re.match(r'unitList_*', i[0]):
                unitList.append(i[1])
                n += 1
                orderList.append(n)


        for i in range(len(procedureList)):
            corporationinformation = Order.objects.create(
                order=orderList[i],
                procedure =procedureList[i],
                material =materialList[i],
                amount=amountList[i],
                unit=unitList[i],
                recipe_id= Recipe.objects.order_by('created_at').last().pk
            )
            corporationinformation.save()
        return redirect(to='/recipe-list')


class RecipeListView(LoginRequiredMixin,generic.ListView):
    model = Recipe
    template_name = 'recipe_list.html'
    paginate_by = 3

    def get_queryset(self, **kwargs):
        queryset = super().get_queryset(**kwargs)
        query = self.request.GET
        list = [0, 0]

        if q := query.get('q'):  # python3.8以降
            if q == '':
                list[0] = 0
            else:
                list[0] = 1

        if p := query.get('p'):
            if p == '':
                list[1] = 9
            else:
                list[1] = 2

        if (list[0] == 1) and (list[1] == 2):
            queryset = queryset.filter(Q(method__icontains=q) & Q(title__icontains=p))

        elif (list[0] == 1) and (list[1] != 2):
            queryset = queryset.filter(Q(method__icontains=q))

        elif (list[0] != 1) and (list[1] == 2):
            queryset = queryset.filter(Q(title__icontains=p))

        elif (list[0] == 0) and (list[1] == 2):
            queryset = queryset.filter(Q(title__icontains=p))

        return queryset.order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # {'pk':{'count':ポストに対するイイネ数,'is_user_liked_for_post':bool},}という辞書を追加していく
        d = {}
        for recipe in self.object_list:
            # postに対するイイね数
            like_for_recipe_count = recipe.likeforrecipe_set.count()
            # ログイン中のユーザーがイイねしているかどうか
            is_user_liked_for_recipe = False
            if not self.request.user.is_anonymous:
                if recipe.likeforrecipe_set.filter(user=self.request.user).exists():
                    is_user_liked_for_recipe = True

            d[recipe.pk] = {'count': like_for_recipe_count, 'is_user_liked_for_recipe': is_user_liked_for_recipe}
        context['recipe_like_data'] = d
        return context

class RecipeCreateView(LoginRequiredMixin,generic.CreateView):
    model = Recipe
    form_class = RecipeCreateForm
    template_name = 'recipe_create.html'
    success_url = reverse_lazy('oniokoze:order_create')

    def form_valid(self, form):
        spot = form.save(commit=False)
        spot.user = self.request.user
        spot.save()
        messages.success(self.request, '日記を作成しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "日記の作成に失敗しました。")
        return super().form_invalid(form)

class RecipeDetailView(LoginRequiredMixin, generic.DetailView):
    model = Recipe
    template_name = 'recipe_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        like_for_recipe_count = self.object.likeforrecipe_set.count()
         # ポストに対するイイね数
        context['like_for_recipe_count'] = like_for_recipe_count
         # ログイン中のユーザーがイイねしているかどうか
        is_user_liked_for_recipe = False
        if not self.request.user.is_anonymous:
            if self.object.likeforrecipe_set.filter(user=self.request.user).exists():
                is_user_liked_for_recipe = True
        context['is_user_liked_for_recipe'] = is_user_liked_for_recipe
        return context


def like_for_recipe(request):
    recipe_pk = request.POST.get('recipe_pk')
    context = {
        'user': f'{request.user.last_name} {request.user.first_name}',
    }
    recipepost = get_object_or_404(Recipe, pk=recipe_pk)
    like = LikeForRecipe.objects.filter(target=recipepost, user=request.user)
    if like.exists():
        like.delete()
        context['method'] = 'delete'
    else:
        like.create(target=recipepost, user=request.user)
        context['method'] = 'create'

    context['like_for_recipe_count'] = recipepost.likeforrecipe_set.count()

    return JsonResponse(context)

class RecipeUpdateView(LoginRequiredMixin, FuckYouMixin, generic.UpdateView):
    model = Recipe
    template_name = 'recipe_update.html'
    form_class = RecipeCreateForm

    def get_success_url(self):
        return reverse_lazy('oniokoze:recipe_detail', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        messages.success(self.request, '日記を更新しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "日記の更新に失敗しました。")
        return super().form_invalid(form)


class RecipeDeleteView(LoginRequiredMixin, FuckYouMixin, generic.DeleteView):
    model = Recipe
    template_name = 'recipe_delete.html'
    success_url = reverse_lazy('oniokoze:recipe_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "日記を削除しました。")
        return super().delete(request, *args, **kwargs)

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
        n=1
        id=Catch.objects.order_by('created_at').last().pk
          # request.POST.items()でPOSTで送られてきた全てを取得。
        for i in request.POST.items():
            if re.match(r'titleList_*', i[0]):
                titleList.append(i[1])
            if re.match(r'bodyList_*', i[0]):
                bodyList.append(i[1])

            noList.append(n)
            n+=1

        for i in range(len(titleList)):
            corporationinformation = Fishname.objects.create(
                name= titleList[i],
                size = bodyList[i],
                no = noList[i],
                catch_id= id
            )
            corporationinformation.save()
        return redirect(to='/catch-list')

class FishCreateView(generic.CreateView):
    form_class = FishCreateForm
    template_name = 'fish_create.html'
    success_url = reverse_lazy('oniokoze:spot_create')

    def post(self, request, *args, **kwrgs):
          # 空の配列を作ります
        fishList= []
        noList= []
        idList= []
        n=1
          # request.POST.items()でPOSTで送られてきた全てを取得。
        for i in request.POST.items():
            if re.match(r'fishList_*', i[0]):
                fishList.append(i[1])

            noList.append(n)
            n+=1

        for i in range(len(fishList)):
            corporationinformation = Fish.objects.create(
                fish= fishList[i],
                no = noList[i],
                spot_id= Spot.objects.order_by('created_at').last().pk
            )
            corporationinformation.save()
        return redirect(to='/spot-list')

class FishnameUpdateView(generic.UpdateView):
        template_name = 'fishname_update.html'
        model = Fishname
        form_class = FishnameCreateForm
        def get_success_url(self):
            id = Fishname.catch
            # return reverse_lazy('oniokoze:catch_detail',kwargs={'pk':self.kwargs['pk']})
            return  reverse_lazy('oniokoze:mypage')
        def form_valid(self, form):
            messages.success(self.request,'項目を更新しました')
            return super().form_valid(form)
        def form_invalid(self, form):
            messages.error(self.request,'項目の更新に失敗しました')
            return super().form_invalid(form)

class OrderUpdateView(generic.UpdateView):
    template_name = 'order_update.html'
    model = Order
    form_class = OrderCreateForm

    def get_success_url(self):
        id = Order.recipe
        return reverse_lazy('oniokoze:mypage')

    def form_valid(self, form):
        messages.success(self.request, '項目を更新しました')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, '項目の更新に失敗しました')
        return super().form_invalid(form)

class FishUpdateView(generic.UpdateView):
    template_name = 'fish_update.html'
    model = Fish
    form_class = FishCreateForm

    def get_success_url(self):
        id = Fish.spot
        return reverse_lazy('oniokoze:mypage')

    def form_valid(self, form):
        messages.success(self.request, '項目を更新しました')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, '項目の更新に失敗しました')
        return super().form_invalid(form)

class TriviaView(generic.TemplateView):
    template_name = 'trivia.html'
class MypageView(generic.TemplateView):
    template_name = 'mypage.html'


class ToolView(generic.TemplateView):
    template_name = 'tool.html'
class MannersView(generic.TemplateView):
    template_name = 'manners.html'
class BaitView(generic.TemplateView):
    template_name = 'bait.html'

class Fishing_methodView(generic.TemplateView):
    template_name = 'fishing_method.html'

class Dangerous_creatureView(generic.TemplateView):
    template_name = 'dangerous_creature.html'

class PlaceView(generic.TemplateView):
    template_name = 'Place.html'

class MypageDetailView(LoginRequiredMixin,GotoHellMixin, generic.DetailView):
    model = CustomUser
    template_name = 'mypage_detail.html'
class MypageUpdateView(LoginRequiredMixin,GotoHellMixin, generic.UpdateView):
    model = CustomUser
    template_name = 'mypage_update.html'
    form_class = MypageCreateForm

    def get_success_url(self):
        return reverse_lazy('oniokoze:mypage_detail', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        messages.success(self.request, '日記を更新しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "日記の更新に失敗しました。")
        return super().form_invalid(form)


class MyCatchListView(LoginRequiredMixin, generic.ListView):
    model = Catch
    template_name = 'mycatch_list.html'
    def get_queryset(self):
        mycatchs= Catch.objects.filter(user=self.request.user).order_by('-created_at')
        return mycatchs


class MyRecipeListView(LoginRequiredMixin,generic.ListView):
    model = Recipe
    template_name = 'myrecipe_list.html'

    def get_queryset(self):
        myrecipes= Recipe.objects.filter(user=self.request.user).order_by('-created_at')
        return myrecipes

class MySpotLikeView(LoginRequiredMixin,generic.ListView):
    model = LikeForSpot
    template_name = 'myspot_like.html'

    def get_queryset(self):
        spotlikes= LikeForSpot.objects.filter(user=self.request.user).order_by('-timestamp')
        return spotlikes

class MyCatchLikeView(LoginRequiredMixin,generic.ListView):
    model = LikeForCatch
    template_name = 'mycatch_like.html'

    def get_queryset(self):
        catchlikes= LikeForCatch.objects.filter(user=self.request.user).order_by('-timestamp')
        return catchlikes

class MyRecipeLikeView(LoginRequiredMixin,generic.ListView):
    model = LikeForRecipe
    template_name = 'myrecipe_like.html'

    def get_queryset(self):
        recipelikes= LikeForRecipe.objects.filter(user=self.request.user).order_by('-timestamp')
        return recipelikes