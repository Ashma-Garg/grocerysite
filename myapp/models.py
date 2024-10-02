from django.db import models
import datetime
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Type(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return f"Type is {self.name}"


class Item(models.Model):
    type = models.ForeignKey(Type, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=100)
    available = models.BooleanField(default=True)
    description = models.TextField(blank=True, null=True)
    def __str__(self):
        return f"Item {self.id} of {self.type} type"


class Client(User):
    CITY_CHOICES = [('WD', 'Windsor'),('TO', 'Toronto'),('CH', 'Chatham'),('WL', 'WATERLOO')]
    # fullname = models.CharField(max_length=50)
    shipping_address = models.CharField(max_length=300, null=True, blank=True)
    city=models.CharField(max_length=2, choices=CITY_CHOICES, default='CH')
    interested_in = models.ManyToManyField(Type)
    phone_number = models.CharField(blank=True, max_length=10)
    def __str__(self):
        return f"Client {self.id} from {self.city}"


class OrderItem(models.Model):
    # ForeignKey to Item model (assuming it exists in the same or a different app)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    
    # ForeignKey to Client model (assuming it exists in the same or a different app)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    
    # Field for the number of items ordered
    quantity = models.IntegerField()

    # Field for order status with choices
    ORDER_STATUS_CHOICES = [
        (0, 'Cancelled'),
        (1, 'Placed'),
        (2, 'Shipped'),
        (3, 'Delivered'),
    ]
    status = models.IntegerField(choices=ORDER_STATUS_CHOICES, default=1)
    
    # Date field for when the order was last updated
    last_updated = models.DateField(auto_now=True)

    def __str__(self):
        return f"Order {self.id} by {self.client}"
    
    def total_price(self):
        # Assuming `price` field exists in the Item model
        return self.quantity * self.item.price