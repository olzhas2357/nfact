from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import Shop, Cart, CartItem
from .forms import AddToCartForm

def home(request):
    shop = Shop.objects.all()
    return render(request, 'home.html', {'shop': shop})

def details(request, pk):
    try:
        card = Shop.objects.get(pk=pk)
    except Shop.DoesNotExist:
        raise Http404('Shop does not exist')
    
    form = AddToCartForm(initial={'product_id': card.id})
    return render(request, 'details.html', {'card': card, 'form': form})

def add_to_cart(request):
    if request.method == 'POST':
        form = AddToCartForm(request.POST)
        if form.is_valid():
            product = get_object_or_404(Shop, pk=form.cleaned_data['product_id'])
            quantity = form.cleaned_data['quantity']
            
            cart, created = Cart.objects.get_or_create(id=request.session.get('cart_id', None))
            if created:
                request.session['cart_id'] = cart.id

            cart_item, created = CartItem.objects.get_or_create(product=product)
            if not created:
                cart_item.quantity += quantity
            else:
                cart_item.quantity = quantity
            cart_item.save()
            cart.items.add(cart_item)
            return redirect('cart_detail')
    return redirect('home')


def cart_detail(request):
    try:
        cart = Cart.objects.get(id=request.session.get('cart_id'))
    except Cart.DoesNotExist:
        cart = None
    return render(request, 'cart_detail.html', {'cart': cart})