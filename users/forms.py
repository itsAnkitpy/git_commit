from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"
        exclude = ["likeability", 'user','blocked_by']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['full_name', 'age', 'gender', 'os', 'editor', 'tech_stack', 'bio','spacing']
        widgets = {
            'tech_stack': forms.Select(attrs={'class': 'form-control','required': False}),
            # ... other widgets ...
        }