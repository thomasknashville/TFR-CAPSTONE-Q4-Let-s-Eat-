from django import forms

class SignupForm(forms.Form):
  username = forms.CharField(widget=forms.TextInput())
  email = forms.EmailField()
  password = forms.CharField(widget=forms.PasswordInput)

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput)