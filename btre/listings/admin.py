from django.contrib import admin

from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display =('id','title','is_published','price','list_date','realtor') #these come from the model definition
    list_display_links=('id','title') #id and title will be linkable
    list_filter = ('realtor',)
    list_editable = ('is_published',)
    search_fields = ('title','description','address','city','state','zipcode','price')
    list_per_page = 25


admin.site.register(Listing, ListingAdmin)
