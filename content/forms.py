from django import forms

from content.models import Publication


class PublicationForm(forms.ModelForm):
    class Meta:
        model = Publication
        exclude = ('author', 'number_views',)
