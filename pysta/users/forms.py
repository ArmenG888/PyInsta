from django import forms

themes =(
    ("1", "light"),
    ("2", "dark"),
)
  
class SettingsForm(forms.Form):
    username = forms.CharField()
    image = forms.ImageField(required=False)
    theme = forms.ChoiceField(choices=themes)
    bio = forms.CharField()
