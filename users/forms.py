from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from users.models import User


class UserRegisterForm(UserCreationForm):
    """
    Представление формы регистрации
    """
    class Meta:
        model = User
        fields = ('phone', 'password1', 'password2')


class UserProfileForm(UserChangeForm):
    """
    Представление изменения профиля пользователя
    """
    class Meta:
        model = User
        fields = ('phone', 'email', 'first_name', 'last_name', 'avatar', 'city')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget = forms.HiddenInput()
