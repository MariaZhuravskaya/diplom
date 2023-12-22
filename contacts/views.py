
from django.views.generic import ListView
from contacts.models import Contact


class ContactListView(ListView):
    model = Contact
    # context_object_name = 'contacts'
    #
    # def get_queryset(self):
    #     return Contact.objects.all()
