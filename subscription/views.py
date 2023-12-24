from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from subscription.forms import SubscriptionForm
from subscription.models import Subscription


class SubscriptionListView(ListView):
    """
    Модель списка подписки
    """
    model = Subscription

    def get_queryset(self):
        """
        Метод предоставляет список подписок пользователя
        """
        queryset = super().get_queryset()
        queryset = queryset.filter(user_id=self.request.user.id)
        return queryset


class SubscriptionCreateView(CreateView):
    """
    Модель создания подписки
    """
    model = Subscription
    form_class = SubscriptionForm
    success_url = reverse_lazy('payments:payments_form')

    def form_valid(self, form):
        self.object = form.save()
        self.object.user = self.request.user
        if self.object.payments:
            self.object.is_active = True
            self.object.save()
            return super().form_valid(form)
        else:
            self.object.save()
            return super().form_valid(form)
