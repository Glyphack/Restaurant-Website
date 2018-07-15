from django.urls import path

from . import views

app_name = 'foodsapp'
urlpatterns = [
    # ex: /polls/
    path('', views.index_view, name='index'),
    path('login/', views.login, name='login'),
    # ex: /polls/5/
    path('user/<int:user_id>/neworder/', views.newOrder, name='order'),
    # ex: /polls/5/results/
    path('user/<int:user_id>/profile/', views.userProfile, name='profile'),
    path('user/<int:user_id>/profile/edit/', views.userProfileEdit, name='edit'),
    path('user/<int:user_id>/orders/', views.userOrders, name='orders'),
    # ex: /polls/5/vote/
    path('foods/', views.foods, name='menu'),
    path('foods/<int:id>/', views.product_detail, name='detail')
]