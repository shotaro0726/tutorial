from django import forms

class ClaimForm(forms.Forms):
    name = forms.CharField(label='なまえ',max_length=100,required=False)
    email = forms.EmailField(label='メールアドレス')
    text = forms.CharField(label='クレーム内容', widget=forms.Textarea)
