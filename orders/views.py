from django.shortcuts import render, redirect
from .models import OrderItem, Order
from .forms import OrderCreateForm
from cart.cart import Cart
from users.decorators import customer_required
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
import requests
import json
from django.http import HttpResponse
from suds.client import Client

ZARINPAL_WEBSERVICE = 'https://sandbox.zarinpal.com/pg/services/WebGate/wsdl'
MMERCHANT_ID = 'XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX'
amount = 0

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
            global amount
            print(type(int(cart.get_total_price())))
            print(type(amount))
            print(int(cart.get_total_price()))
            amount = 100
            description = u'test'  # Required
            email = 'user@userurl.ir'  # Optional
            mobile = '09123456789'  # Optional
            CallbackURL = 'http://127.0.0.1:8000/orders/verify/'
            client = Client(ZARINPAL_WEBSERVICE)
            result = client.service.PaymentRequest(
                                                    MMERCHANT_ID,
                                                    amount,
                                                    description,
                                                    email,
                                                    mobile,
                                                    CallbackURL)
            if result.Status == 100:
                cart.clear()
                return redirect('https://sandbox.zarinpal.com/pg/StartPay/' + result.Authority)
            else:
                return HttpResponse('Error')
        return render(request, 'order/created.html', {'order': order})
    else:
        form = OrderCreateForm()
    return render(request, 'order/create.html', {'form': form})

def verify(request):
    client = Client(ZARINPAL_WEBSERVICE)
    if request.GET.get('Status') == 'OK':
        result = client.service.PaymentVerification(MMERCHANT_ID,
                                                    request.GET['Authority'],
                                                    amount)
        if result.Status == 100:
            return HttpResponse('Transaction success. RefID: ' + str(result.RefID))
        elif result.Status == 101:
            return HttpResponse('Transaction submitted : ' + str(result.Status))
        else:
            return HttpResponse('Transaction failed. Status: ' + str(result.Status))
    else:
        return HttpResponse('Transaction failed or canceled by user')

class OrderListView(ListView):
    template_name = 'order/all_orders.html'
    context_object_name = 'orders_list'
    
    def get_queryset(self):
        return Order.objects.order_by('-created')[:]