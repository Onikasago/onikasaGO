import logging
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from.models import Catch
from django.shortcuts import get_object_or_404

logger = logging.getLogger(__name__)

class IndexView(generic.TemplateView):
    template_name = "index.html"


class OniokozeCreateView(LoginRequiredMixin, generic.CreateView):
    model = Oniokoze
    template_name = 'oniokoze_create.html'
    form_class = OniokozeCreateForm
    success_url = reverse_lazy('oniokoze:oniokoze_list')

    def form_valid(self, form):
        oniokoze = form.save(commit=False)
        oniokoze.user = self.request.user
        oniokoze.save()
        messages.success(self.request, '日記を作成しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "日記の作成に失敗しました。")
        return super().form_invalid(form)


