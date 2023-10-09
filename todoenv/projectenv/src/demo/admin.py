from django.contrib import admin
from demo.models import Product

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    #displaying list
    list_display = ("name","sku","price",) 
    #search bar implementation
    search_fields = ("name",)
    #Filtering draft.publish,block
    list_filter = ("status",)


