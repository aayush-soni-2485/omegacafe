from django.shortcuts import render, redirect
from .models import Product, Cart

# Create your views here.

def home(request):
    items = Product.objects.all()
    return render(request, 'home.html', {'items': items})

def add_to_cart(request):
    item_id = request.POST.get('item_id')
    product = Product.objects.get(id=item_id)

    cart_item, created = Cart.objects.get_or_create(
        user=request.user,
        product=product
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('/orders/')

def orders(request):
    cart_items = Cart.objects.filter(user=request.user)
    return render(request, 'orders.html', {'cart_items': cart_items})

def about(request):
    return render(request, 'about.html')

def increase_qty(request, id):
    cart = Cart.objects.get(id=id)
    cart.quantity += 1
    cart.save()
    return redirect('/orders/')


def decrease_qty(request, id):
    cart = Cart.objects.get(id=id)

    if cart.quantity > 1:
        cart.quantity -= 1
        cart.save()
    else:
        cart.delete()

    return redirect('/orders/')


def remove_item(request, id):
    Cart.objects.get(id=id).delete()
    return redirect('/orders/')