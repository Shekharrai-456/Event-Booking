from django.urls import path
from .views import payment_process, payment_success, payment_failure
urlpatterns = [
    path('<int:booking_id>/', payment_process, name='payment-process'),
    path('<int:booking_id>/success/', payment_success, name='payment-success'),
    path('<int:booking_id>/failure/', payment_failure, name='payment-failure'),
]