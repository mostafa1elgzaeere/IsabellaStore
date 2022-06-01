from django.contrib import admin
from django.urls import path

from .views import Contact, Faqs, home ,products ,product_detil,About

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('',home,name="home"),
    path('products/<slug:name_categorey>/',products,name="products"),

    path('products/<str:name_categorey>/<str:product_name>/',product_detil,name="product_choice"),
    
    path('faqs/',Faqs,name="faqs"),
    path('about/',About,name="about"),
    path('contact/',Contact,name="contact"),


]
