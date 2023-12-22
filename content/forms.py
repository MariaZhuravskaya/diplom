from django import forms
from content.models import Publication


class PublicationForm(forms.ModelForm):
    """
    Форма создания публикации
    """
    class Meta:
        model = Publication
        exclude = ('author', 'number_views',)
