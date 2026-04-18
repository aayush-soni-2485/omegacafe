from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('add-to-cart/', views.add_to_cart),
    path('orders/', views.orders),
    path('about/', views.about),

    path('increase/<int:id>/', views.increase_qty),
    path('decrease/<int:id>/', views.decrease_qty),
    path('remove/<int:id>/', views.remove_item),
]