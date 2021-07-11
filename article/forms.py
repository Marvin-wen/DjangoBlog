from django import forms
from .models import ArticlePost


class ArticlePostForm(forms.ModelForm):
    class Meta:
        model = ArticlePost  # 指明数据模型的来源
        fields = ('title', 'body')  # 定义表单包含的字段
