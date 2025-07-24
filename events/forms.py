from django import forms
from .models import Event, EventGallery
from django.forms import inlineformset_factory
class EventForm(forms.ModelForm):
    start_datetime = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        input_formats=['%Y-%m-%dT%H:%M']
    )
    end_datetime = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        input_formats=['%Y-%m-%dT%H:%M']
    )
    
    class Meta:
        model = Event
        exclude = ('organizer', 'status', 'created_at', 'updated_at')
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5}),
            'categories': forms.CheckboxSelectMultiple(),
        }
class EventGalleryForm(forms.ModelForm):
    class Meta:
        model = EventGallery
        fields = ('image', 'caption')
EventGalleryFormSet = inlineformset_factory(
    Event, EventGallery, 
    form=EventGalleryForm,
    extra=3,
    can_delete=True
)
class EventApprovalForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('status',)
        widgets = {
            'status': forms.Select(attrs={'class': 'form-control'})
        }