from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        #fields = '__all__'
        exclude = ('post_user', 'post_title','post_content', 'post_date',)
     