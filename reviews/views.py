from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ReviewForm
from events.models import Event

# Create your views here.
@login_required
def review_create(request, event_pk):
    event = get_object_or_404(Event, pk=event_pk)
    
    # Check if user has already reviewed or attended the event
    if Review.objects.filter(user=request.user, event=event).exists():
        messages.warning(request, 'You have already reviewed this event.')
        return redirect('event-detail', pk=event_pk)
    
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.event = event
            review.save()
            messages.success(request, 'Thank you for your review!')
            return redirect('event-detail', pk=event_pk)
    else:
        form = ReviewForm()
    
    return render(request, 'reviews/create.html', {
        'form': form,
        'event': event
    })