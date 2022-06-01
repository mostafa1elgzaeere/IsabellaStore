from django.urls import path
from order.views import create_order
urlpatterns = [
    path('create_order',create_order,name="create_order")
]