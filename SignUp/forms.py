from django.forms import ModelForm
from .models import SignUp

class SignUpForm(ModelForm):
    class Meta:
        model = SignUp
