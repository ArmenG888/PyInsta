from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

themes =(
    ("1", "light"),
    ("2", "dark"),
)
  
class SettingsForm(forms.Form):
    username = forms.CharField()
    image = forms.ImageField(required=False)
    theme = forms.ChoiceField(choices=themes)
    bio = forms.CharField()
    website = forms.CharField()
    full_name = forms.CharField()
