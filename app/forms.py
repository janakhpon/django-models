from django import forms
from app.models import User

class NewUser(forms.ModelForm):
    """docstring for NewUser."""
    class Meta:
        model = User
        fields = '__all__'
