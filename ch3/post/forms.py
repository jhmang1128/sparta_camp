from django import forms
from .models import Post

# class ArticleForm(forms.Form):
#     title = forms.CharField(max_length=50)
#     content = forms.CharField(widget=forms.Textarea)
    
class Post_form(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        # exclude = ('created_at', 'updated_at')