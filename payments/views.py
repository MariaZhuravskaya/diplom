from datetime import datetime
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, TemplateView
from config import settings
from content.models import Publication
from payments.models import Payments
import stripe
from subscription.models import Subscription

stripe.api_key = settings.API_KEY_STRIPE_SECRET


class PaymentsListView(ListView):
    """
    Модель списка платежей
    """
    model = Payments

    def get_queryset(self):
        """
        Метод предоставляет список платежей пользователя
        """
        queryset = super().get_queryset()
        queryset = queryset.filter(user_id=self.request.user.id)
        return queryset


class CreateCheckoutSessionView(View):

    def get(self, request, *args, **kwargs):
        if self.request.user.is_anonymous:
            return HttpResponseRedirect(reverse_lazy('users:register'))
        publication = Publication.objects.get(id=self.kwargs["pk"])
        domain = "https://yourdomain.com"
        if settings.DEBUG:
            domain = "http://127.0.0.1:8000"

        product = stripe.Product.create(name=publication.name)
        price = stripe.Price.create(
            unit_amount=int(publication.price * 100),
            currency="usd",
            product=product.id,
        )

        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price': price,
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=domain + '/payments/success/?session_id={CHECKOUT_SESSION_ID}',
            cancel_url=domain + '/payments/cancel/',
            metadata={'publicationId': publication.id}
        )

        return redirect(checkout_session.url)


class SuccessView(TemplateView):
    template_name = "payments/success.html"

    def get(self, request, *args, **kwargs):
        session_id = request.GET.get('session_id')
        checkout_session = stripe.checkout.Session.retrieve(session_id)

        publication_id = checkout_session.metadata['publicationId']
        publication = Publication.objects.get(id=int(publication_id))

        payment = Payments(publication=publication, user=self.request.user, date=datetime)

        payment.save()

        subscription = Subscription(publication=publication,
                     user=self.request.user,
                     payments=payment,
                     is_active=True)

        subscription.save()

        return super().get(request, *args, **kwargs)


class CancelView(TemplateView):
    template_name = "cancel.html"
