from django import forms

themes =(
    ("1", "light"),
    ("2", "dark"),
)
  
class ThemeForm(forms.Form):
    theme = forms.ChoiceField(choices=themes)

