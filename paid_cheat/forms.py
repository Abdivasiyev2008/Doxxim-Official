from django import forms
from .models import *

class NewCommentForm(forms.ModelForm):
    class Meta:
        model = BlogComment
        fields = ('content',)