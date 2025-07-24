from django.urls import path
from .views import event_list, event_detail, event_create, event_approval
urlpatterns = [
    path('', event_list, name='event-list'),
    path('<int:pk>/', event_detail, name='event-detail'),
    path('create/', event_create, name='event-create'),
    
    # Admin-only URLs
    path('<int:pk>/approve/', event_approval, name='event-approval'),
]
