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




class CatchList(generic.ListView):
    model = Catch

class CatchCreateView(generic.CreateView):
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
