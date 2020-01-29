from django.shortcuts import render
from property.models import Property

def home(request):
    context = {
        'latest_property' : Property.objects.filter(uniqueness__name='Latest'),
        'offer_property' : Property.objects.filter(uniqueness__name='Offer').first(),
        'rent_apartment' : Property.objects.filter(status__name='For Rent', category__name='Apartment')[:4],
        'sale_property' : Property.objects.filter(status__name='For Sale')[:4]
    }
    return render(request, 'loxpack/index.html', context)

def about(request):
    return render(request, 'loxpack/about.html')

def pproperty(request, pk):
    stat = Property.objects.get(pk=pk).status
    context = {
        'property' : Property.objects.get(pk=pk),
        'stats' : Property.objects.filter(status__name=stat)
    }
    return render(request, 'loxpack/property.html', context)

def sale(request):
    context = {
        'sale_property' : Property.objects.filter(status__name='For Sale')
    }
    return render(request, 'loxpack/sale.html', context)

def rent(request):
    context = {
        'rent_apartment' : Property.objects.filter(status__name='For Rent')
    }
    return render(request, 'loxpack/rent.html', context)
   
def contact(request):
    return render(request, 'loxpack/contact.html')

