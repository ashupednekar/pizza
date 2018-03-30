from django.shortcuts import render
from django.http import HttpResponse
from .forms import orderForm


def rendrer(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = orderForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            pizza = form.cleaned_data['pizza']
            name = form.cleaned_data['name']
            address = form.cleaned_data['address']
            phone = form.cleaned_data['phone']

            return render(request, 'success.html', {'pizza':pizza, 'name':name, 'address':address, 'phone':phone})
            
    # if a GET (or any other method) we'll create a blank form
    else:
        form = orderForm()

    return render(request, 'index.html', {'form': form})

