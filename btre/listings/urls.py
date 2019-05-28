from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='listings'), #Index in the listing app
    path('<int:listing_id>', views.listing, name='listing'),
    path('search', views.search, name='search'),
]