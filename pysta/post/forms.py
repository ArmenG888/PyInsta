from django import forms

class PostForm(forms.Form):
    image = forms.ImageField(label="image")
    description = forms.CharField(max_length=5000, required=False, widget=forms.Textarea)

