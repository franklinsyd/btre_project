from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Listing
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import price_choices,bedroom_choices,state_choices


def index(request):
    #listings = Listing.objects.all() #Get all listings from the database
    listings = Listing.objects.order_by('-list_date').filter(is_published=True) # - is to order in descending order
    
    # filter(is_published=True) checks in the databased of the is_published field is set or not

    paginator = Paginator(listings, 6)  #Handles the pagination
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    #pass them in the context variable
    context = {
        'listings': paged_listings   #here, you could pass listings directly if you don't need pagination
    }
    return render(request, 'listings/listings.html', context)  #from the  app template folder

def listing(request, listing_id):

    #get the listing by listing_id
    listing = get_object_or_404(Listing, pk=listing_id)
    
    #listing = Listing.objects.get(id=listing_id)  # Conventional all

    context = {
        'listing': listing
    }
    return render(request, 'listings/listing.html', context)

def search(request):

    queryset_list = Listing.objects.order_by('-list_date') #get all data from database
    
    #Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords) # description__icontains double underscore
    
    #City
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city) # city__icontains double underscore


   #State
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(state__iexact=state) # state__icontains double underscore
   #Bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms) # state__icontains double underscore
    
    #Price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price) # price__icontains double underscore
    
    context = {
        'state_choices':state_choices,
        'bedroom_choices':bedroom_choices,
        'price_choices':price_choices,
        'listings': queryset_list,
        'values': request.GET
    }

    return render(request, 'listings/search.html', context)