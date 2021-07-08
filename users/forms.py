from django import forms

from users.models import TFRUser

class AddUserProfile(forms.Form):
    email = forms.EmailField(null=True, blank=True)
    bio = forms.TextField(max_length=250)