from django.shortcuts import render

from django.http import HttpResponse

from listings.models import Listing
from realtors.models import Realtor

from listings.choices import type_choices, bedroom_choices, bathroom_choices, sqft_choices, state_choices, price_choices

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:4]
    realtors = Realtor.objects.order_by('-hire_date')
    context = {
        'listings': listings,
        'realtors': realtors,
        'type_choices': type_choices,
        'bedroom_choices': bedroom_choices,
        'bathroom_choices': bathroom_choices,
        'sqft': sqft_choices,
        'state_choices': state_choices,
        'price_choices': price_choices,
    }
    return render(request, 'pages/index.html', context)

def about(request):
    return render(request, 'pages/about.html')

