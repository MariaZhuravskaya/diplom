from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import Permission
from django.http import Http404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView

from content.forms import PublicationForm
from content.models import Publication
from users.models import User


def index(request):
    if request.method == 'GET':
        context = {
            'publication': Publication.objects.order_by('?')[:3]
        }
        return render(request, 'content/index.html', context)


class PublicationCreateView(CreateView):
    model = Publication
    form_class = PublicationForm
    success_url = reverse_lazy('content:publication_list')

    def form_valid(self, form):
        self.object = form.save()
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)


class PublicationListView(ListView):
    model = Publication

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_publication=True)
        return queryset


class PublicationUpdateView(UpdateView):
    model = Publication
    form_class = PublicationForm
    success_url = reverse_lazy('content:publication_list')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.author != self.request.user and not self.request.user.is_staff:
            raise Http404
        return self.object


class PublicationDetailView(DetailView):
    model = Publication

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.number_views += 1
        self.object.save()
        return self.object


class PublicationDeleteView(DeleteView):
    model = Publication
    success_url = reverse_lazy('content:publication_list')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.author != self.request.user and not self.request.user.is_staff:
            raise Http404
        return self.object
