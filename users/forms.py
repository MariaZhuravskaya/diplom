from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from users.models import User


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('phone', 'password1', 'password2')


class UserProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('phone', 'email', 'first_name', 'last_name', 'avatar', 'city')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget = forms.HiddenInput()

#
# class PasswordResetRequestForm(forms.Form):
#     email = forms.EmailField()
#
#     def clean_email(self):
#         email = self.cleaned_data.get('email')
#         user = User.objects.filter(email=email).first()
#         if not user:
#             raise forms.ValidationError('Пользователь с таким email адресом не найден.')
#         return email
