from django import forms
from users.models import Image

from users.models import TFRUser

class SignupForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput)


# class ProfileForm(forms.Form):
#     email = forms.EmailField(null=True, blank=True)
#     bio = forms.TextField(max_length=250, blank=True)


class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Image
        fields = ('title', 'image')
