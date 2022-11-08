import logging
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CatchCreateForm
from .models import Catch
from django.contrib import messages
from django.urls import reverse_lazy


logger = logging.getLogger(__name__)

class IndexView(generic.TemplateView):
    template_name = "index.html"


class CatchListView(LoginRequiredMixin, generic.ListView):
    model = Catch
    template_name = 'catch_list.html'

    def get_queryset(self):
        catches = Catch.objects.filter(user=self.request.user).order_by('-created_at')
        return catches


class CatchCreateView(LoginRequiredMixin, generic.CreateView):
    model = Catch
    template_name = 'catch_create.html'
    form_class = CatchCreateForm
    success_url = reverse_lazy('oniokoze:oniokoze_list')

    def form_valid(self, form):
        catch = form.save(commit=False)
        catch.user = self.request.user
        catch.save()
        messages.success(self.request, '釣果を作成しました')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "釣果の作成に失敗しました。")





