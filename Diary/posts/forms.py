from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','content'] #'__all__' 대신 넣으면 모든 필드를 불러올수 있음
        