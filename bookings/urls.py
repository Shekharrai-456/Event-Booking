from django.urls import path
from .views import booking_create, booking_confirmation, my_bookings
urlpatterns = [
    path('event/<int:event_pk>/', booking_create, name='booking-create'),
    path('confirmation/<int:booking_id>/', booking_confirmation, name='booking-confirmation'),
    path('my-bookings/', my_bookings, name='my-bookings'),
]