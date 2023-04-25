from django.db import models

# Create your models here.
class Address(models.Model):
    addId = models.AutoField(primary_key=True)
    shop_Flat_House_No= models.CharField(max_length=5)
    street_Address = models.CharField(max_length=20)
    landmark = models.CharField(max_length=60)
    pincode = models.CharField(max_length=10) 
    city = models.CharField(max_length=60)
    state = models.CharField(max_length=60)
    country = models.CharField(max_length=60)

    def __str__(self):
        return self.street_Address
    
class Seller(models.Model):
    sellerID = models.AutoField(primary_key=True)
    sellerName = models.CharField(max_length=160)
    sellerShopName = models.CharField(max_length=160)
    sellerContact = models.CharField(max_length=12)
    sellerEmail = models.EmailField(unique=True)

    def __str__(self):
        return self.sellerName

class Customer(models.Model):
    customerId = models.AutoField(primary_key=True)
    CustomerName = models.CharField(max_length=160)
    CustomerContact = models.CharField(max_length=12)
    CustomerEmail = models.EmailField(unique=True)

    def __str__(self):
        return self.CustomerName

class Category(models.Model):
    categoryId = models.AutoField(primary_key=True)
    categoryName = models.CharField(max_length=160)
    categoryDescription = models.TextField()
    categoryDateAdded = models.DateTimeField(auto_now_add=True)
    categoryLastUpdated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.categoryName
    
class Inventory(models.Model):
    inventoryId = models.AutoField(primary_key=True)
    BatchNumber = models.CharField(max_length=20)
    stock = models.DecimalField(max_digits=10, decimal_places=2)
    BatchPrice = models.DecimalField(max_digits=10, decimal_places=2)
    dateAdded = models.DateTimeField()
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.BatchNumber
    
class Product(models.Model):
    productId = models.AutoField(primary_key=True)
    productName = models.CharField(max_length=160)
    productDescription = models.TextField()
    productQuantity = models.DecimalField(max_digits=10, decimal_places=2)
    productImage =  models.ImageField(upload_to='Products/')
    productPrice =  models.DecimalField(max_digits=10, decimal_places=2)
    productWeight = models.DecimalField(max_digits=10, decimal_places=2)
    productOfferPrice = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    productDiscount = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    productStatus = models.CharField(max_length=20)
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)

    def __str__(self):
        return self.productName
    
class Cart(models.Model):
    cartId = models.AutoField(primary_key=True)
    productQuantity = models.DecimalField(max_digits=10, decimal_places=2)
    productTotalAmount = models.DecimalField(max_digits=10, decimal_places=2)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.customer.CustomerName}'s Cart"
    # def get_total_price(self):
    #     return self.productQuantity * self.productTotalAmount



class Order(models.Model):
    orderId = models.AutoField(primary_key=True)
    orderQuantity = models.DecimalField(max_digits=10, decimal_places=2)
    orderCoupon = models.CharField(max_length=20, null=True)
    orderTotalAmount = models.DecimalField(max_digits=10, decimal_places=2)
    orderStatus = models.CharField(max_length=20)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.customer.CustomerName}'s orders"

class Coupon(models.Model):
    couponId = models.AutoField(primary_key=True)
    couponCode = models.CharField(max_length=20)
    couponStatus = models.CharField(max_length=60)
    couponText = models.TextField()
    couponDiscountType = models.CharField(max_length=100)
    couponDateAdded = models.DateTimeField(auto_now_add=True)
    couponLastUpdated = models.DateTimeField(auto_now_add=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.order.orderCoupon}'s coupons"
    
class Payment(models.Model):
    paymentId = models.AutoField(primary_key=True)
    paymentMethod = models.CharField(max_length=100)
    cc_Type = models.CharField(max_length=100, null=True)
    cc_Type = models.CharField(max_length=100, null=True)
    cc_Owner = models.CharField(max_length=100, null=True)  
    cc_Number = models.CharField(max_length=100,null=True)
    cc_Expiry = models.CharField(max_length=100, null=True)
    paymentStatus = models.CharField(max_length=100)
    paymentDate = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.customer.CustomerName}'s Payment"

class Delivery(models.Model):
    deliveryId = models.AutoField(primary_key=True)
    deliveryDate = models.DateTimeField()
    deliveryTime = models.DateTimeField()
    deliveryCharges = models.DecimalField(max_digits=10, decimal_places=2)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE) 
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    Customer =  models.ForeignKey(Customer, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.Customer.CustomerName}'s Delivery"

class Order_Item(models.Model):
    orderItemId = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product.productName}'s Order_item"
    


class Wishlist(models.Model):
    wishlistId = models.AutoField(primary_key=True)
    product =models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    

    def __str__(self):
        return f"{self.customer.CustomerName}'s Wishlist"

class Review(models.Model):
    reviewId = models.AutoField(primary_key=True)
    comments = models.TextField()
    rating = models.IntegerField()
    seller =  models.ForeignKey(Seller, on_delete=models.CASCADE)
    delivery =  models.ForeignKey(Delivery, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.customer.CustomerName}'s Review" 