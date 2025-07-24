from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import EventList, EventDetail
urlpatterns = [
    path('events/', EventList.as_view(), name='event-list-api'),
    path('events/<int:pk>/', EventDetail.as_view(), name='event-detail-api'),
]
urlpatterns = format_suffix_patterns(urlpatterns)