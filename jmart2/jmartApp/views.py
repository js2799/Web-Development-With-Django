# from django.shortcuts import render
from rest_framework import generics
from .models import Address
from .models import Seller
from .models import Customer
from .models import Category
from .models import Inventory
from .models import Product
from .models import Cart
from .models import Order
from .models import Coupon
from .models import Payment
from .models import Delivery
from .models import Order_Item
from .models import Wishlist
from .models import Review

from .serializers import AddressSerilizer
from .serializers import SellerSerilizer
from .serializers import CustomerSerilizer
from .serializers import CategorySerilizer
from .serializers import InventorySerilizer
from .serializers import ProductSerilizer
from .serializers import CartSerilizer
from .serializers import OrderSerilizer
from .serializers import CouponSerilizer
from .serializers import PaymentSerilizer
from .serializers import DeliverySerilizer
from .serializers import Order_ItemSerilizer
from .serializers import WishlistSerilizer
from .serializers import ReviewSerilizer


# Create your views here.
class AddressGetCreate(generics.ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerilizer

class AddressUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerilizer
#
class SellerGetCreate(generics.ListCreateAPIView):
    queryset = Seller.objects.all()
    serializer_class = SellerSerilizer

class SellerUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Seller.objects.all()
    serializer_class = SellerSerilizer
#
class CustomerGetCreate(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerilizer 

class CustomerUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerilizer
#
class CategoryGetCreate(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerilizer

class CategoryUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerilizer

#
class InventoryGetCreate(generics.ListCreateAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerilizer

class InventoryUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerilizer
#
class ProductGetCreate(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerilizer

class ProductUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerilizer
#
class CartGetCreate(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerilizer

class CartUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerilizer

#
class OrderGetCreate(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerilizer

class OrderUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerilizer

#
class CouponGetCreate(generics.ListCreateAPIView):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerilizer

class CouponUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerilizer

#
class PaymentGetCreate(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerilizer

class PaymentUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerilizer 

#
class DeliveryGetCreate(generics.ListCreateAPIView):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerilizer

class DeliveryUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerilizer
#
class Order_ItemGetCreate(generics.ListCreateAPIView):
    queryset = Order_Item.objects.all()
    serializer_class = Order_ItemSerilizer

class Order_ItemUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order_Item.objects.all()
    serializer_class = Order_ItemSerilizer
#
class WishlistGetCreate(generics.ListCreateAPIView):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerilizer

class WishlistUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerilizer
#
class ReviewGetCreate(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerilizer

class ReviewUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerilizer