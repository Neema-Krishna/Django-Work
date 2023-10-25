from django import forms
from .models import Comments

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comments
        fields='__all__'
        exclude=['post']
        labels={'user_name':'Your Name',
                'email':'Your Email',
                'text':'Your Comment'}