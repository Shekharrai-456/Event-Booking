# users/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser 
class CustomUser (AbstractUser ):
    USER_TYPE_CHOICES = (
        ('customer', 'Customer'),
        ('organizer', 'Event Organizer'),
        ('admin', 'Admin')
    )
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES, default='customer')
    phone = models.CharField(max_length=15, blank=True)
    # Specify related_name to avoid clashes
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # Change this to avoid clashes
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',  # Change this to avoid clashes
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )
    class Meta:
        verbose_name = 'Custom User'
        verbose_name_plural = 'Custom Users'
class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser , on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    bio = models.TextField(blank=True)
    website = models.URLField(blank=True)
    social_media = models.JSONField(default=dict)
    email_verified = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.user.username}'s Profile"