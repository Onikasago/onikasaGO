import logging
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
import re
from .forms import CatchCreateForm, FishnameCreateForm,CatchFormset
from .models import Catch, Fishname
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models.functions import Upper
from django.db.models.query import QuerySet
from django.contrib import messages
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

logger = logging.getLogger(__name__)

global var
var=0
class IndexView(generic.TemplateView):
    template_name = "index.html"


class CatchListView(LoginRequiredMixin, generic.ListView):
    model = Fishname.objects.select_related('catch').all()
    template_name = 'catch_list.html'
    paginate_by = 4

    def get_queryset(self):
        catches = Catch.objects.filter(user=self.request.user).order_by('-created_at')
        return catches


class OnlyYouMixin(UserPassesTestMixin):
    raise_exception = True

    def test_func(self):
        catch = get_object_or_404(Catch, pk=self.kwargs['pk'])
        return self.request.user == list.user


class CatchDetailView(LoginRequiredMixin, generic.DetailView):
    catches= Catch.objects.values_list('id')
    model = Fishname.objects.select_related('catch')
    model = Catch
    template_name = 'catch_detail.html'

    def get_queryset(self):
        catches = Fishname.objects.select_related('catch')

        return catches

class CatchCreateView(LoginRequiredMixin,generic.ListView):
    model = Catch


def catch_create(request):
    form = CatchCreateForm(request.POST or None)
    context = {'form':form}
    if request.method == 'POST' and form.is_valid():
        post = form.save(commit=False)
        formset = CatchFormset(request.POST,instance=post)
        if formset.is_valid():
            post.save()
            formset.save()
            return redirect('oniokoze:catch')
    else:
        context['formset'] = CatchFormset()

    return render(request, 'catch_create.html' , context)



def form_valid(self, form):
    catch = form.save(commit=False)
    catch.user = self.request.user
    var = catch.id
    catch.save()
    return redirect(self.success_url)



class FishnameCreateView(generic.CreateView):
    form_class = FishnameCreateForm
    template_name = 'fishname_create.html'

    def post(self, request, *args, **kwrgs):
          # 空の配列を作ります
        formList = []
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
            if re.match(r'noList_*', i[0]):
                noList.append(n)
            if re.match(r'idList_*', i[0]):
                idList.append(var)
            n+=1
        for i in range(len(titleList)):
            corporationinformation = Fishname.objects.create(
                name= titleList[i],
                size = bodyList[i],
                no = noList[i],
                catch_id= idList[i],
            )
            corporationinformation.save()
        return redirect(to='/catch-list')

class SpotListView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'spot_list.html'


class ResipeListView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'resipe_list.html'


class TriviaView(generic.TemplateView):
    template_name = 'trivia.html'


class MypageView(generic.TemplateView):
    template_name = 'mypage.html'
