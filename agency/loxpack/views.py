from django.shortcuts import render
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

class SearchResultsView(View):
    #model = Property
    #template_name = 'loxpack/search_results.html'

    def get(self, *args, **kwargs):
        qs =  Property.objects.all()
        query1 = self.request.GET.get('q1') #Tassia
        query2 = self.request.GET.get('q2') #For Rent

        if query1 and query2:
            qs = qs.filter(Q(area__name__icontains=query1)) | Q(status__name__icontains=query2)
        if query1 == '' and query2 == '':
            messages.warning(self.request, 'No Property selected')
            return redirect('/')
        if qs is None:
            messages.warning(self.request, f'No Property Named{query1}')
            return redirect('/')    
        context = {
            'search_query_rslt' : qs
        }
        return render(self.request, 'loxpack/search_results.html', context)     

  