from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import Order ,OrderItem
# Register your models here.


#old way
# admin.site.register(Order)
# admin.site.register(OrderItem)


'''
1- TabularInline [to collect more tables in one page] in child
    in child : model = 
    

2- ModelAdmin [to filter and chose dispaly fields ] in parent
    in parent  : list_display = ['','','']
              : list_filters = ['','','']
              : inlines=[childAdminClass,]


3- admin.site.register(ParentModel,ParentAdminClass)              
'''
#child
class OrderItemAdmin(admin.TabularInline):
    model=OrderItem



#parent
class OrderAdmin(ModelAdmin):
    list_display=['first_name','last_name','address','city','postal_code','paid','created_at','updated_at']
    list_filter=['city','paid','created_at','updated_at']     
    inlines=[OrderItemAdmin,]


admin.site.register(Order,OrderAdmin)
