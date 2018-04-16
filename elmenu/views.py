from django.shortcuts import render
from django.http import HttpResponse
from .forms import orderForm
from .models import OrderHist

order = OrderHist()


def rendrer(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = orderForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            order.pizza = form.cleaned_data['pizza']
            order.name = form.cleaned_data['name']
            order.address = form.cleaned_data['address']
            order.phone = form.cleaned_data['phone']
            order.save()
            return render(request, 'success.html', {'pizza':order.pizza, 'name':order.name, 'address':order.address, 'phone':order.phone})
            
    # if a GET (or any other method) we'll create a blank form
    else:
        form = orderForm()

    return render(request, 'index.html', {'form': form})

