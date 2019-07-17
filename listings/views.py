from django.shortcuts import get_object_or_404, render

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from listings.choices import type_choices, bedroom_choices, bathroom_choices, area_choices, state_choices, price_choices

from .models import Listing

def index(request):
    listings = Listing.objects.order_by('-list_date')

    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings
    }
    return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    # tile = [
    #     listing
    # ]
    context = {
        'listing': listing,
    }

    return render(request, 'listings/listing.html', context)
    
def search(request):
    queryset_list = Listing.objects.order_by('-list_date')
    
    #keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)
    
    #property-type
    if 'house_type' in request.GET:
        house_type= request.GET['house_type']
        if house_type:
            queryset_list = queryset_list.filter(house_type__iexact=house_type)

    #bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)

    #bathrooms
    if 'bathrooms' in request.GET:
        bathrooms = request.GET['bathrooms']
        if bathrooms:
            queryset_list = queryset_list.filter(bathrooms__lte=bathrooms)

    #area
    if 'area' in request.GET:
        area = request.GET['area']
        if area:
            queryset_list = queryset_list.filter(area__lte=area)

    #state
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(state__iexact=state)

    #price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)

    context = {
        'type_choices': type_choices,
        'bedroom_choices': bedroom_choices,
        'bathroom_choices': bathroom_choices,
        'area_choices': area_choices,
        'state_choices': state_choices,
        'price_choices': price_choices,
        'listings': queryset_list
    }
    return render(request, 'listings/search.html', context)
    