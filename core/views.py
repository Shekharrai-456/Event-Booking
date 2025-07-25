# core/views.py
from django.views.generic import TemplateView
from events.models import Event  # Import the Event model
from .forms import ContactForm
class HomeView(TemplateView):
    template_name = 'core/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['featured_events'] = Event.objects.filter(status='approved').order_by('-start_datetime')[:3]
        return context