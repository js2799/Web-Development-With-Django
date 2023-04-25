from django.contrib import admin
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

# Register your models here.
admin.site.register(Address)
admin.site.register(Seller)
admin.site.register(Customer)
admin.site.register(Category)
admin.site.register(Inventory)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(Coupon)
admin.site.register(Payment)
admin.site.register(Delivery)
admin.site.register(Order_Item)
admin.site.register(Wishlist)
admin.site.register(Review)