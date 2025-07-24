from django import forms
from .models import Booking, Ticket
from events.models import Event
class BookingForm(forms.ModelForm):
    event = forms.ModelChoiceField(
        queryset=Event.objects.filter(status='approved'),
        widget=forms.HiddenInput()
    )
    
    class Meta:
        model = Booking
        fields = ('event', 'additional_info')
        widgets = {
            'additional_info': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Special requests or requirements'})
        }
class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ('ticket_type', 'quantity', 'attendee_name', 'attendee_email')
        widgets = {
            'attendee_name': forms.TextInput(attrs={'placeholder': 'Name as it appears on ticket'}),
            'attendee_email': forms.EmailInput(attrs={'placeholder': 'Email for ticket confirmation'}),
        }
TicketFormSet = forms.inlineformset_factory(
    Booking, Ticket,
    form=TicketForm,
    extra=1,
    can_delete=False
)