from django.urls import path
from .views import AddressGetCreate, AddressUpdateDelete
from .views import SellerGetCreate, SellerUpdateDelete
from .views import CustomerGetCreate, CustomerUpdateDelete
from .views import CategoryGetCreate, CategoryUpdateDelete
from .views import InventoryGetCreate, InventoryUpdateDelete
from .views import ProductGetCreate, ProductUpdateDelete
from .views import CartGetCreate, CartUpdateDelete
from .views import OrderGetCreate, OrderUpdateDelete
from .views import CouponGetCreate, CouponUpdateDelete
from .views import PaymentGetCreate, PaymentUpdateDelete
from .views import DeliveryGetCreate, DeliveryUpdateDelete
from .views import Order_ItemGetCreate, Order_ItemUpdateDelete
from .views import WishlistGetCreate, WishlistUpdateDelete
from .views import ReviewGetCreate, ReviewUpdateDelete

urlpatterns = [
    path('address',AddressGetCreate.as_view()),
    path('address/<int:pk>',AddressUpdateDelete.as_view()),

    path('seller',SellerGetCreate.as_view()),
    path('seller/<int:pk>',SellerUpdateDelete.as_view()),

    path('customer',CustomerGetCreate.as_view()),
    path('customer/<int:pk>',CustomerUpdateDelete.as_view()),

    path('category',CategoryGetCreate.as_view()),
    path('category/<int:pk>',CategoryUpdateDelete.as_view()),

    path('inventory',InventoryGetCreate.as_view()),
    path('inventory/<int:pk>',InventoryUpdateDelete.as_view()),

    path('product',ProductGetCreate.as_view()),
    path('product/<int:pk>',ProductUpdateDelete.as_view()),

    path('cart',CartGetCreate.as_view()),
    path('cart/<int:pk>',CartUpdateDelete.as_view()),
    
    path('order',OrderGetCreate.as_view()),
    path('order/<int:pk>',OrderUpdateDelete.as_view()),

    path('coupon',CouponGetCreate.as_view()),
    path('coupon/<int:pk>',CouponUpdateDelete.as_view()),

    path('payment',PaymentGetCreate.as_view()),
    path('payment/<int:pk>',PaymentUpdateDelete.as_view()),

    path('delivery',DeliveryGetCreate.as_view()),
    path('delivery/<int:pk>',DeliveryUpdateDelete.as_view()),

    path('orderitem',Order_ItemGetCreate.as_view()),
    path('orderitem/<int:pk>',Order_ItemUpdateDelete.as_view()),

    path('wishlist',WishlistGetCreate.as_view()),
    path('wishlist/<int:pk>',WishlistUpdateDelete.as_view()),

    path('review',ReviewGetCreate.as_view()),
    path('review/<int:pk>',ReviewUpdateDelete.as_view()),

    
]