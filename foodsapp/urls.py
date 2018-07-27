from django.urls import path

from . import views

app_name = 'foodsapp'
urlpatterns = [
    # ex: /polls/
    path('', views.index_view, name='index'),
    path('foods/', views.foods, name='menu'),
    path('foods/<int:id>/', views.product_detail, name='detail')
]