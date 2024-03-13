from django import forms
from .models import UserMovie,Review

class MovieForm(forms.ModelForm):
    class Meta:
        model=UserMovie
        fields=['title','description','actors','youtube_link','category','date','image']

    def __init__(self, *args, **kwargs):
        super(MovieForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class ReviewForm(forms.ModelForm):
    class Meta:
        model=Review
        fields = ["comment", "rating"]