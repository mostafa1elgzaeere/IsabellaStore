from django.shortcuts import redirect, render
from cart.forms import ProductForm
from .cart  import Cart
from store.models import Product
from django.views.decorators.http import require_POST


# Create your views here.


def add_in_cart(request,product_id):
    cart=Cart(request)  # get object from class to cach the session
    product=Product.objects.get(id=product_id)   #filter current product
    form=ProductForm(request.POST)                  


    if form.is_valid(): 
            cd = form.cleaned_data
            cart.add(product=product, quantity=cd['quantity'],update_quantity=cd['update'])
   

    return redirect('cart_detail')    



@require_POST
def remove_from_cart(request,product_id):
    cart=Cart(request)  # get object from class to cach the session
    product=Product.objects.get(id=product_id)   #filter current product
    cart.remove(product)    # delete key py this name
    return redirect('cart_detail') 


def cart_detail(request):
    cart = Cart(request)
    form=ProductForm(request.POST)                  

    for item in cart:
        item['update_quantity_form'] = ProductForm(
            initial={'quantity': item['quantity'], 'update': True})

    
    return render(request, 'cart_detial.html', {'cart': cart,'form':form})
    



