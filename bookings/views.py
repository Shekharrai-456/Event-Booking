from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import BookingForm, TicketFormSet
from events.models import Event

# Create your views here.

@login_required
def booking_create(request, event_pk):
    event = get_object_or_404(Event, pk=event_pk)
    
    if request.method == 'POST':
        form = BookingForm(request.POST)
        formset = TicketFormSet(request.POST)
        
        if form.is_valid() and formset.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.event = event
            booking.total_amount = sum(
                ticket_data['quantity'] * ticket_data['price']
                for ticket_data in formset.cleaned_data
                if ticket_data and not ticket_data.get('DELETE', False)
            )
            booking.save()
            
            instances = formset.save(commit=False)
            for instance in instances:
                instance.booking = booking
                instance.save()
            
            messages.success(request, 'Booking successful!')
            return redirect('booking-confirmation', booking_id=booking.id)
    else:
        form = BookingForm(initial={'event': event})
        formset = TicketFormSet(queryset=Ticket.objects.none())
    
    return render(request, 'bookings/create.html', {
        'form': form,
        'formset': formset,
        'event': event
    })
@login_required
def booking_confirmation(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id, user=request.user)
    return render(request, 'bookings/confirmation.html', {'booking': booking})
@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user).order_by('-booking_date')
    return render(request, 'bookings/list.html', {'bookings': bookings})