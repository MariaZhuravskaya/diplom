from django.urls import path
from payments.views import PaymentsListView, CancelView, SuccessView, CreateCheckoutSessionView

urlpatterns = [

    path('', PaymentsListView.as_view(), name='payments_list'),
    path('cancel/', CancelView.as_view(), name='cancel'),
    path('success/', SuccessView.as_view(), name='success'),
    path('create-checkout-session/<pk>/', CreateCheckoutSessionView.as_view(), name='create-checkout-session')
]
