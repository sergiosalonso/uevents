from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction
from .models import User, Profile

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=250, required=True)
    USER_TYPE_CHOICES = (
        ('s', 'Student'),
        ('t', 'Teacher' ),
    )
    choices = forms.ChoiceField(choices=USER_TYPE_CHOICES)

    class Meta(UserCreationForm.Meta):
        model= User
        fields=('username', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este email ya existe, prueba con otro.")
        return email

    def save(self):
        choices = self.cleaned_data.get("choices")
        user = super().save(commit=False)
        user.save()
        profile = Profile.objects.create(user=user, type_user=choices)
        profile.save()
        return user


class ProfileUpdateForm(forms.ModelForm):
        model=Profile
        fields = ('bio', 'profile_image')
