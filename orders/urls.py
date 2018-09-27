from django.conf.urls import url
from . import views

app_name = 'orders'

urlpatterns = [
    url(r'^create/$', views.order_create, name='order_create'),
    url(r'^verify/$', views.verify, name='verify'),
    url(r'^allorders/$', views.OrderListView.as_view(), name='order_list')
]