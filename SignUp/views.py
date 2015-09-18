from django.shortcuts import render
from .forms import SignUpForm
# Create your views here.

def register(requset):

    context = {
                form = SignUpForm
            }
    return render(request, 'signup.html', context)

