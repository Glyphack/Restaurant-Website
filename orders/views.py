from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from users.decorators import customer_required
from django.contrib.auth.decorators import login_required

@login_required
@customer_required
def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        # form.fields['address'] = request.user.customer.address
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )
            cart.clear()
        return render(request, 'order/created.html', {'order': order})
    else:
        form = OrderCreateForm(request = request)
    return render(request, 'order/create.html', {'form': form})