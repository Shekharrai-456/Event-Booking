from django.db import models
from users.models import CustomUser
from events.models import Event

# Create your models here.

class Booking(models.Model):
    STATUS_CHOICES = (
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
        ('attended', 'Attended')
    )
    
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    booking_reference = models.CharField(max_length=20, unique=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='confirmed')
    booking_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=8, decimal_places=2)
    is_paid = models.BooleanField(default=False)
    additional_info = models.TextField(blank=True)
    def __str__(self):
        return f"{self.user.username} - {self.event.title}"
    
    
class Ticket(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, related_name='tickets')
    ticket_type = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.PositiveIntegerField()
    attendee_name = models.CharField(max_length=100)
    attendee_email = models.EmailField()
    qr_code = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return f"Ticket #{self.id} for {self.booking}"