from django.views import View
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class BaseView(PermissionRequiredMixin, SuccessMessageMixin, View):

    raise_exception = True
    permission_required = []

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class BaseListView(BaseView, ListView):

    paginate_by = 10


class BaseCreateView(BaseView, CreateView):

    pass


class BaseUpdateView(BaseView, UpdateView):

    slug_field = 'uuid'
    slug_url_kwarg = 'uuid'


class BaseDeleteView(BaseView, DeleteView):

    slug_field = 'uuid'
    slug_url_kwarg = 'uuid'

    def delete(self, request, *args, **kwargs):
        messages.success(request, self.success_message)
        return super(BaseDeleteView, self).delete(request, *args, **kwargs)


class BaseDetailView(BaseView, DetailView):

    slug_field = 'uuid'
    slug_url_kwarg = 'uuid'
