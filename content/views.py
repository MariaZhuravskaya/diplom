from django.http import Http404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView
from content.forms import PublicationForm
from content.models import Publication


def index(request):
    if request.method == 'GET':
        context = {
            'publication': Publication.objects.order_by('?')[:3]
        }
        return render(request, 'content/index.html', context)


class PublicationCreateView(CreateView):
    """
    Представление для создания публикации
    """
    model = Publication
    form_class = PublicationForm
    success_url = reverse_lazy('content:publication_list')

    def form_valid(self, form):
        """
        Метод автозаполнения поля автора в модели при создании публикации
        """
        self.object = form.save()
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)


class PublicationListView(ListView):
    """
    Представление списка публикаций
    """
    model = Publication

    def get_queryset(self, *args, **kwargs):
        """
        Метод отдает список опубликованных (с флагом is_publication=True) публикации
        """
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_publication=True)
        return queryset


class PublicationUpdateView(UpdateView):
    """
    Представление для изменений публикации
    """
    model = Publication
    form_class = PublicationForm
    success_url = reverse_lazy('content:publication_list')

    def get_object(self, queryset=None):
        """
        Метод разрешает вносить изменения в публикации, только автору и администратору
        """
        self.object = super().get_object(queryset)
        if self.object.author != self.request.user and not self.request.user.is_staff:
            raise Http404
        return self.object


class PublicationDetailView(DetailView):
    """
    Представление для просмотра публикации
    """
    model = Publication

    def get_object(self, queryset=None):
        """
        Метод подсчета просмотров публикации
        """
        self.object = super().get_object(queryset)
        self.object.number_views += 1
        self.object.save()
        return self.object


class PublicationDeleteView(DeleteView):
    """
    Представление для удаления публикации
    """
    model = Publication
    success_url = reverse_lazy('content:publication_list')

    def get_object(self, queryset=None):
        """
        Метод разрешает удалять публикацию, только автору и администратору
        """
        self.object = super().get_object(queryset)
        if self.object.author != self.request.user and not self.request.user.is_staff:
            raise Http404
        return self.object
