from django.urls import path
from . import views as v 



urlpatterns = [
    path('carts-list/', v.CartsListAPIView.as_view(), name='carts-list'),
    path('cart-edit/<int:pk>/', v.CartUpdateDeleteAPIView.as_view(), name='cart-edit'),
]