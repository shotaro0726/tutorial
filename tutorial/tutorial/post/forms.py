from django import forms
from .models import Post

class ClaimForm(forms.Form):
    name = forms.CharField(label='なまえ',max_length=100)
    email = forms.EmailField(label='メールアドレス')
    text = forms.CharField(label='クレーム内容', widget=forms.Textarea)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('name','naiyou')
