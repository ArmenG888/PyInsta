from django import forms

class PostForm(forms.Form):
    image = forms.ImageField(label="image")
    description = forms.CharField(max_length=5000, required=False, widget=forms.Textarea)

class CommentForm(forms.Form):
    text = forms.CharField()

class ReplyForm(forms.Form):
    relpytext = forms.CharField()

class EditForm(forms.Form):
    description = forms.CharField(max_length=500, required=False, widget=forms.Textarea)