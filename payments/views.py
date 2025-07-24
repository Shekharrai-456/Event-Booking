from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from bookings.models import Booking

# Create your views here.
@login_required
def payment_process(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id, user=request.user)
    
    if booking.is_paid:
        messages.warning(request, 'This booking has already been paid.')
        return redirect('booking-confirmation', booking_id=booking.id)
    
    if request.method == 'POST':
        # Simulate payment processing
        booking.is_paid = True
        booking.save()
        
        # Create payment record
        Payment.objects.create(
            booking=booking,
            amount=booking.total_amount,
            payment_method='dummy',
            transaction_id=f'DUMMY-{booking.id}-{request.user.id}',
            status=True
        )
        
        messages.success(request, 'Payment processed successfully!')
        return redirect('payment-success', booking_id=booking.id)
    
    return render(request, 'payments/process.html', {'booking': booking})
def payment_success(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id, user=request.user)
    return render(request, 'payments/success.html', {'booking': booking})
def payment_failure(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id, user=request.user)
    return render(request, 'payments/failure.html', {'booking': booking})