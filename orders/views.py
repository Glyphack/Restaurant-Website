from time import time

from suds.client import Client

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.http import HttpResponse
from django.conf import settings

from .models import OrderItem, Order
from .forms import OrderCreateForm
from cart.cart import Cart
from users.decorators import customer_required


ZARINPAL_WEBSERVICE = settings
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
            # amount = cart.get_total_price unknown issue with zarrinpal api will be fixed
            amount = 100
            email = request.user.email
            mobile = '09123456789' #didn't used this field in database it's here just because of the zarrinpal api
            description = u'food'
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
            context = {
                'status': result.RefID,
                'message': 'با موفقیت انجام شد'
            }
            return render(request, 'order/verify.html', context)
        elif result.Status == 101:
            context = {
                'status': result.Status,
                'message': 'ثبت شد'
            }
            return render(request, 'order/verify.html', context)

        else:
            context = {
                'status': result.Status,
                'message': 'با شکست مواجه شد دوباره امتحان کنید'
            }
            return render(request, 'order/verify.html', context)
    else:
            context = {
                'message': 'توسط کاربر کنسل شد'
            }
            return render(request, 'order/verify.html', context)

class OrderListView(ListView):
    template_name = 'order/all_orders.html'
    context_object_name = 'orders_list'
    
    def get_queryset(self):
        return Order.objects.order_by('-created')[:]