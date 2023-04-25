from rest_framework import serializers
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

class AddressSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

class SellerSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = '__all__'

class CustomerSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class CategorySerilizer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class InventorySerilizer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = '__all__'

class ProductSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CartSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

class OrderSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class CouponSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = '__all__'

class PaymentSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

class DeliverySerilizer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = '__all__'

class Order_ItemSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Order_Item
        fields = '__all__'

class WishlistSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = '__all__'

class ReviewSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'