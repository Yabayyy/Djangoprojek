from django.shortcuts import render
from datetime import datetime

# Create your views here.
def index(request):
    context_dict = {'text': 'halo kamu yang baca', 'number': 20000, 'now': datetime.now() }
    return render(request, 'basapp/index.html', context=context_dict)

def profile(request):
    return render(request, 'basapp/profile.html' )

def contact(request):
    return render(request, 'basapp/contact.html' )