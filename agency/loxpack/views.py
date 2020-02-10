from django.shortcuts import render, redirect
from property.models import Property, Area, Status
from django.contrib import messages
from django.views.generic import ListView, View
from django.db.models import Q

def home(request):
    context = {
        'latest_property' : Property.objects.filter(uniqueness__name='Latest'),
        'offer_property' : Property.objects.filter(uniqueness__name='Offer').first(),
        'rent_apartment' : Property.objects.filter(status__name='For Rent', category__name='Apartment')[:4],
        'sale_property' : Property.objects.filter(status__name='For Sale')[:4],
        'props' : Property.objects.all()[:4],
        'location' : Area.objects.all(),
        'stats' : Status.objects.all()
    }
    return render(request, 'loxpack/index.html', context)

def about(request):
    context = {
        'text' : 'About Loxpack' 
    }
    return render(request, 'loxpack/about.html', context)

def pproperty(request, pk):
    stat = Property.objects.get(pk=pk).status
    context = {
        'property' : Property.objects.get(pk=pk),
        'location' : Area.objects.all(),
        'stat' : Property.objects.filter(status__name=stat),
        'stats' : Status.objects.all(),
        'text' : 'Property Details',   
    }
    return render(request, 'loxpack/property.html', context)

def sale(request):
    context = {
        'sale_property' : Property.objects.filter(status__name='For Sale'),
        'text' : 'Property For Sale', 
        'location' : Area.objects.all(),
        'stats' : Status.objects.all()  
    }
    return render(request, 'loxpack/sale.html', context)

def rent(request):
    context = {
        'rent_apartment' : Property.objects.filter(status__name='For Rent'),
        'text' : 'Property For Rent', 
        'location' : Area.objects.all(),
        'stats' : Status.objects.all()  
    }
    return render(request, 'loxpack/rent.html', context)
   
def contact(request):
    context ={
        'text' : 'Contact Us',
        'location' : Area.objects.all(),
        'stats' : Status.objects.all()   
    }
    return render(request, 'loxpack/contact.html', context)

def is_valid_queryparam(param1, param2):
    return param1 != '' and param2 != '' and param1 is not None and param2 is not None

def search_results(request):
    qs = Property.objects.all()
    loc_contains_query = request.GET.get('loc_contains')
    stat_contains_query = request.GET.get('stat_contains')


    if is_valid_queryparam(loc_contains_query, stat_contains_query) and loc_contains_query != 'Select Location' and stat_contains_query != 'For Rent/Sale':
        qs = qs.filter(Q(area__name__icontains=loc_contains_query) & Q(status__name__icontains=stat_contains_query)).distinct()

    elif loc_contains_query == 'Select Location' and stat_contains_query == 'For Rent/Sale':
        messages.warning(request, 'Nothing Selected')

    context = {
        'search_query_rslt' : qs,
        'similar_search' : Property.objects.filter(status__name=stat_contains_query),
        'text' : 'Search Results', 
        'location' : Area.objects.all(),
        'stats' : Status.objects.all() 
    }  


    return render(request, 'loxpack/search_results.html', context)

  