from django.urls import path
from content.views import index, PublicationCreateView, PublicationListView, PublicationDetailView, \
    PublicationUpdateView, PublicationDeleteView

urlpatterns = [
    path('', index),
    path('publication/create', PublicationCreateView.as_view(), name='publication_form'),
    path('publication', PublicationListView.as_view(), name='publication_list'),
    path('publication/detail/<int:pk>', PublicationDetailView.as_view(), name='publication_detail'),
    path('publication/update/<int:pk>', PublicationUpdateView.as_view(), name='publication_update'),
    path('publication/delete/<int:pk>', PublicationDeleteView.as_view(), name='publication_delete'),
]
