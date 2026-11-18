from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django import forms

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ("username", "email", "skin_type", "skin_triggers")
        
    def clean_skin_triggers(self):
        triggers = self.cleaned_data.get('skin_triggers')
        if triggers:
            trigger_list = [t.strip() for t in triggers.split(',') if t.strip()]
            if not (1 <= len(trigger_list) <= 10):
                raise forms.ValidationError("You must enter between 1 and 10 skin triggers.")
        return triggers

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ("email", "skin_type", "skin_triggers")