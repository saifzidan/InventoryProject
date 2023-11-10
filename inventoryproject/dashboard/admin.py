from django.contrib import admin
from .models import Product , Order
admin.site.site_header = 'Inventory'
admin.site.site_title = 'Inventory'
admin.site.index_title_title = 'Inventory'
class productAdmin(admin.ModelAdmin):
    list_display = ('name' , 'category' , 'quantity')
    list_filter = ('category' , )
    search_fields = ('name' , 'quantity')
class orderAdmin(admin.ModelAdmin):
    list_display = ('id' , 'product' , 'staff' , 'order_quantity')
    list_filter = ('staff' , )
    search_fields = ('staff' , 'product')
admin.site.register(Product , productAdmin)
admin.site.register(Order , orderAdmin)