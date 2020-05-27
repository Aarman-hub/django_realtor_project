from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from listings.choices import bedroom_choices, price_choices, states_choices

# Create your views here.
from .models import *

def index(request):
    listings = Listing.objects.all()

    paginator = Paginator(listings, 1)
    page    = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {'listings':paged_listings}
    return render(request,'listings/listings.html',context)

def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    context = {'listing':listing}
	
    return render(request,'listings/listing.html',context)
def search(request):
    query_set = Listing.objects.order_by('-list_date')
    
    # keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            query_set = query_set.filter(description__icontains=keywords)

    # city
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            query_set = query_set.filter(city__iexact=city)

    # state
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            query_set = query_set.filter(state__iexact=state)
    
    # bedrooms
    if 'badrooms' in request.GET:
        badrooms = request.GET['badrooms']
        if badrooms:
            query_set = query_set.filter(badrooms__lte=badrooms)


    # price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            query_set = query_set.filter(price__lte=price)

    context = {
    'bedroom_choices':bedroom_choices,
    'price_choices':price_choices,
    'states_choices':states_choices,
    'listings':query_set,
    'values':request.GET,
    }
	
    return render(request, 'listings/search.html', context)