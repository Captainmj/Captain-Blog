from django import forms
from .models import Comments, Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['categroy', 'title', 'body', 'status', 'topped']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['name','comment_body']
