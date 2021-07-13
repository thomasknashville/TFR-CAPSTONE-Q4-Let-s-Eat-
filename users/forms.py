from users.models import TFRUser
from django import forms


class SignupForm(forms.ModelForm):
    class meta:
        model = TFRUser
        fields = (
            'username',
            'email',
            'password'
        )
        
    def __str__(self) -> str:
        return self.name
class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput)
    
class ProfileEditForm(forms.Form):
    bio = forms.CharField(widget=forms.Textarea)
    picture = forms.ImageField(required = False)
    email = forms.EmailField()
