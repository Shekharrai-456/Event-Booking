from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from .forms import EventForm, EventApprovalForm, EventGalleryFormSet
from .models import Event, Category

# Create your views here.

@login_required
def event_list(request):
    events = Event.objects.filter(status='approved').order_by('-start_datetime')
    categories = Category.objects.all()
    return render(request, 'events/list.html', {
        'events': events,
        'categories': categories
    })
def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'events/detail.html', {'event': event})
@login_required
def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.organizer = request.user
            event.save()
            form.save_m2m()  # For many-to-many relationships
            messages.success(request, 'Event created successfully!')
            return redirect('event-detail', pk=event.pk)
    else:
        form = EventForm()
    return render(request, 'events/create.html', {'form': form})
@permission_required('events.change_event')
def event_approval(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        form = EventApprovalForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            messages.success(request, 'Event status updated!')
            return redirect('admin-dashboard')
    else:
        form = EventApprovalForm(instance=event)
    return render(request, 'events/approval.html', {'form': form, 'event': event})