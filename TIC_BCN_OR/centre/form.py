from django.forms import ModelForm
from .models import User

class UserForm(ModelForm):
    class Meta:
        model = User
        # fields = ['nom', 'email', 'rol']
        fields = '__all__'