from django.urls import path
from contacts.views import ContactListView

urlpatterns = [
    path('', ContactListView.as_view(), name='contact_list'),
]
