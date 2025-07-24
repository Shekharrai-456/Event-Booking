from django import forms
from .models import Review
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('rating', 'comment')
        widgets = {
            'comment': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Share your experience...'}),
            'rating': forms.RadioSelect(choices=[(1, '1★'), (2, '2★'), (3, '3★'), (4, '4★'), (5, '5★')])
        }
        labels = {
            'rating': 'Your Rating'
        }