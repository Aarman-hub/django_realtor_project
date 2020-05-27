from django.contrib import admin

from .models import Listing
# Register your models here.
class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','price','realtor','list_date','is_published')
    list_display_link=('id','title','price')
    list_filter = ('realtor',)
    search_fields =('title','description')


admin.site.register(Listing, ListingAdmin)
