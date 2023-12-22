from django.urls import path
from subscription.views import SubscriptionListView, SubscriptionCreateView


urlpatterns = [
    path('subscription/create', SubscriptionCreateView.as_view(), name='subscription_form'),
    path('', SubscriptionListView.as_view(), name='subscription_list'),
]
