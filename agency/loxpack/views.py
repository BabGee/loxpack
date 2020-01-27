from django.shortcuts import render
from property.models import Property

def home(request):
    context = {
        'rent_apartment' : Property.objects.filter(status__name='For Rent', category__name='Apartment'),
        'sale_property' : Property.objects.filter(status__name='For Sale')
    }
    return render(request, 'loxpack/index.html', context)

def about(request):
    return render(request, 'loxpack/about.html')

def pproperty(request, pk):
    context = {
        'property' : Property.objects.get(pk=pk)
    }
    return render(request, 'loxpack/property.html', context)

def sale(request):
    return render(request, 'loxpack/sale.html')

def rent(request):
    return render(request, 'loxpack/rent.html')
   
def contact(request):
    return render(request, 'loxpack/contact.html')

