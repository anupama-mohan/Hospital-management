from django import forms 
from . models import Booking
from .models import Contact

class DateInput(forms.DateInput):
    input_type='date'
    
class BookingForm(forms.ModelForm):
        class Meta:
            model=Booking
            fields='__all__'
            
            widgets={
                'booking_date':
                    DateInput()
            }
            
            labels={
                'p_name':"patient Name:",
                'p_phone':"patient phone Number:",
                'p_email':"patient EmailId:",
                'doc_name':"Doctor Name:",
                'booking_date':"Booking date:"
                
                    
            }
            
class ContactForm(forms.ModelForm):
    
    
    class Meta:
        model = Contact
        fields = ['name','email','message']
    
    