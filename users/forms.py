from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordResetForm
from .models import CustomUser, UserProfile
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=15, required=False)
    user_type = forms.ChoiceField(choices=CustomUser.USER_TYPE_CHOICES)
    
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2', 
                 'first_name', 'last_name', 'phone', 'user_type')
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username or Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    
    error_messages = {
        'invalid_login': "Please enter a correct %(username)s and password.",
        'inactive': "This account is inactive.",
    }
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('bio', 'website', 'social_media', 'profile_picture')
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4}),
            'social_media': forms.TextInput(attrs={'placeholder': '{"twitter": "", "instagram": ""}'}),
        }
class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        label="Email",
        max_length=254,
        widget=forms.EmailInput(attrs={'autocomplete': 'email', 'placeholder': 'Enter your email'})
    )