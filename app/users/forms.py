from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import forms
from django.contrib.auth.admin import User
from .models import Profile

class registerForm(UserCreationForm):
    email = forms.CharField()

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']

    def __init__(self, *args, **kwargs):
        super(registerForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2','email']:
            self.fields[fieldname].help_text = None

class userUpdate(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email']


class updateProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']