from django.urls import path
from .views import review_create
urlpatterns = [
    path('event/<int:event_pk>/review/', review_create, name='review-create'),
]