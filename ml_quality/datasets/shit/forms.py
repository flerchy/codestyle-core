
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy
from ask_app.models import UserProfile


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            'phone',
            'resume',
            'sex',
            'image'
        ]
        labels = {
            'phone': gettext_lazy('Телефон'),
        }
        help_texts = {
            'phone': gettext_lazy('Укажите свой номер телефона. Пример: 380931234567'),
        }
        error_messages = {
            'phone': {
                'max_length': gettext_lazy("Максимальная длинна 12 символов"),
            },
        }
        widgets = {
            'phone': forms.TextInput(attrs={'class': 'input_field'}),
            # 'resume': forms.FileField(attrs={'class': 'xxx'}),
            'sex': forms.Select(attrs={'class': 'input_field'}),
            # 'image': forms.ImageField(),
        }


class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'last_name',
            'email',
            'username',
            'first_name',
            'password'
        ]
        widgets = {
            'password': forms.PasswordInput(attrs={'class': 'input_field'})
        }


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'last_name',
            'email',
            'username',
            'first_name',
            'password'
        ]
        widgets = {
            'password': forms.PasswordInput(attrs={'class': 'input_field'})
        }
