from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User
from .models import Post, profile


class registerForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']

    def __init__(self, *args, **kwargs):
        super(registerForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2', 'email']:
            self.fields[fieldname].help_text = None


class postForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', ]


class updateProfile(forms.ModelForm):
    class Meta:
        model = profile
        fields = ['image']


class registerCustom(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

class calculatorForm(forms.Form):

    number = forms.CharField(widget=forms.NumberInput())
    number2 = forms.CharField(widget=forms.NumberInput())


class updateForm(forms.Form):
    title = forms.CharField()
    body = forms.CharField(widget=forms.Textarea())

