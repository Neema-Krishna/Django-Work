from django import forms

from.models import Review

# class ReviewForm(forms.Form):
#     user_name=forms.CharField(label='Your Name',max_length=20,error_messages={'max_length':'Shortrer Name','required':'Your name must not be empty'})
#     review_text=forms.CharField(label='Your Feedback',widget=forms.Textarea)
#     rating=forms.IntegerField(label='Rating',min_value=1,max_value=5)

class ReviewForm(forms.ModelForm):
    class Meta:
        model=Review
        fields= '__all__'
        exclude=['slug']
        labels={'user_name':'Your Name',"review_text":'Your Feedback',"rating":'Your rating'}
        error_messages={'user_name':{'required':'Your name must not be empty!'}}
