from django.views.generic import ListView
from contacts.models import Contact


class ContactListView(ListView):
    """
    Представление списка контактных данных
    """
    model = Contact
