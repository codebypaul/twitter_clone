from django import forms

# Models
from .models import Tweet

max_tweet_length = 240

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['content']

    def clean_content(self):
        content = self.cleaned_data.get('content')
        if len(content) > max_tweet_length:
            raise forms.ValidationError("This tweet is too long")
        return content