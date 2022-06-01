from django.shortcuts import render

from cart.cart import Cart
from order.forms import OrderForm
from order.models import OrderItem

# Create your views here.


def create_order(request):
    cart= Cart(request)  # to get sessions and data cart
   
    
    if request.method=='POST':
        form=OrderForm(request.POST) # take instance from Form
        if form.is_valid():
            order=form.save()             # data was send to Order model so i'm not import it 

            for item in cart:       # loop in items in cart
                OrderItem.objects.create(
                    item=item['product'],    
                    quantity=item['quantity'],
                    price=item['price'],
                    order=order
                )
            cart.clear()       # to clear data from sessions
          
            return render(request,'order_done.html',{'order':order}) # context order to tell client 
                                                                        # your order id is {{order.id}}


    else:
         form=OrderForm() # take instance from Form To work if request.method=='GET'

         
    return render(request,'create_order.html',{"form":form,"cart":cart})
