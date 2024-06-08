from django import forms
from .models import Flight,User
from django.contrib.auth.forms import UserCreationForm

class FlightForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = ['flight_name', 'from_airport', 'to_airport', 'departure_date', 'departure_time', 'arrival_date', 'arrival_time', 'seat_count']
        widgets = {
            'departure_date': forms.DateInput(attrs={'type': 'date'}),
            'departure_time': forms.TimeInput(attrs={'type': 'time'}),
            'arrival_date': forms.DateInput(attrs={'type': 'date'}),
            'arrival_time': forms.TimeInput(attrs={'type': 'time'}),
        }
        
class MyUserCreationForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2','user_type']