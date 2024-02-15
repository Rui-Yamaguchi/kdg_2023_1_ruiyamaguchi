from django import forms
from .models import Comment

class CommentCreateForm(forms.ModelForm):
    text=forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={
                'placeholder':'投稿に対してコメントを書いてください',
                'rows':10,
                'class':'mx-auto',
                'style':'width:100%',
            }
        )
    )
    class Meta:
        model=Comment
        exclude=('username','target','created_at',)