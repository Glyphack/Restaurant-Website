from django.shortcuts import render
from .models import OrderItem, Order
from .forms import OrderCreateForm
from cart.cart import Cart
from users.decorators import customer_required
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView

@login_required
@customer_required
def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
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
        form = OrderCreateForm()
    return render(request, 'order/create.html', {'form': form})

class OrderListView(ListView):
    template_name = 'order/all_orders.html'
    context_object_name = 'orders_list'
    
    def get_queryset(self):
        return Order.objects.order_by('-created')[:]