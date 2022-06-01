from django.db.models import Model
from django.db.models.deletion import CASCADE
from django.db.models.fields import BooleanField, CharField, DateTimeField, DecimalField, EmailField, PositiveIntegerField, TextField
from django.db.models.fields.related import ForeignKey

from store.models import Product
# Create your models here.


class Order(Model):
    #data about user
    first_name = CharField(max_length=100)
    last_name  = CharField(max_length=100)
    email      = EmailField()

    #data about place
    address     = CharField(max_length=300)
    city        = CharField(max_length=200)
    postal_code = CharField(max_length=200)
    
    #data about sale
    paid        = BooleanField(default=False)
    created_at  = DateTimeField(auto_now_add=True)
    updated_at  = DateTimeField(auto_now=True)


    def __str__(self):
        return f"Order {self.id}"

    # get total cost by loop in get_cost for all items
    def get_total_cost(self):
        for item in self.orderitems.all():
           return sum(item.get_cost)


class OrderItem(Model):

    item    = ForeignKey(Product,on_delete=CASCADE , related_name="orderitems")
    order   = ForeignKey(Order,on_delete=CASCADE,related_name="orderitems")
    quantity= PositiveIntegerField(default=1)
    price   = DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return f"{self.id}"

    #get a cost for this item
    def get_cost(self):
        return self.price * self.quantity




    









