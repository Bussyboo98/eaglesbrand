from django import forms
from eaglesbrandapp.models import *
from django.core import validators
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User



   

class CommentForm(forms.ModelForm):
    user_name = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}))
    comment_content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Type your comment',
        'id': 'usercomment',
        'rows': '4'
    }))
    class Meta:
        model = Comment
        exclude = ['user', 'post']
        # fields = ('content', )


