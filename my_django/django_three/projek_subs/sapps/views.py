from django.shortcuts import render
from sapps.models import Costumer
from sapps.forms import NewSubscriber

# Create your views here.
def index(request):
    return render(request, 'sapps/index.html')

def costumer(request):
    costumer_list = Costumer.objects.order_by('first_name')
    costumer_dict = {'costumer': costumer_list}
    return render(request, 'sapps/costumer.html', context=costumer_dict)

def subscribe(request):
    form = NewSubscriber()
    
    if request.method == 'POST':
        form = NewSubscriber(request.POST)
        
        if form.is_valid():
            form.save(commit=True)
            return costumer(request)
        else:
            print("Error : Form error")
            
    return render(request, 'sapps/subs.html', {'form': form})