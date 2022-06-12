from django import forms
from .models import UserMessages


class User_Message_form(forms.ModelForm):

    class Meta:
        model = UserMessages
        fields = '__all__'
        
