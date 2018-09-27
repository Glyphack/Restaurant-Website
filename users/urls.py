from django.urls import include, path
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from .views import CustomerSignUpView
app_name = 'users'
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    # path('accounts/signup/', SignUpView.as_view(), name='signup'),
    # url(r'^login/$', auth_views.login, name='login'),
    # url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    path('signup/customer/', CustomerSignUpView.as_view(), name='customer_signup'),
]