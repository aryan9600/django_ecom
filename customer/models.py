from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

# Create your models here.
CATEGORIES = (

)

LABELS = (

)


class CustomUser(AbstractBaseUser):
    account_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=1000, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.TextField()


class Wishlist(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)


class OrderHistory(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)


class Address(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pincode = models.CharField(max_length=100)


class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    label = models.CharField(choices=LABEL_CHOICES, max_length=1)
    description = models.TextField()
    reviews = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return self.title


class Cart(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)


    def total_item_price(self):
        return self.quantity * self.item.price

    def total_discount(self):
        return self.quantity * self.item.discount_price

    def amount(self):
        return self.total_item_price() - self.total_discount()



class Order(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    Order_id = models.AutoField(primary_key=True)
    items = models.ManyToManyField(Cart)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    shipping_address = models.ForeignKey('Address', on_delete=models.SET_NULL, blank=True, null=True)
    payment = models.ForeignKey('Payment', on_delete=models.SET_NULL, blank=True, null=True)
    delivered = models.BooleanField(default=False)




