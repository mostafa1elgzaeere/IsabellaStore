from cart.cart import Cart


def cart(request):
    cart=Cart(request)
    return {"cart":cart}
# not using render or redirect to be a global varibale not work in one template only     