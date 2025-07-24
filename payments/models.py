from django.db import models
from bookings.models import Booking

# Create your models here.
class Payment(models.Model):
    PAYMENT_METHODS = (
        ('credit_card', 'Credit Card'),
        ('esewa', 'eSewa'),
        ('khalti', 'Khalti'),
        ('cash', 'Cash On Site')
    )
    
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE, related_name='payment')
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHODS)
    transaction_id = models.CharField(max_length=100)
    payment_date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)  # True for successful payments
    def __str__(self):
        return f"Payment for {self.booking}"