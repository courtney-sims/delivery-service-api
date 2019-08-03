from django.db import models

from phone_field import PhoneField

class Client(models.Model):
    client_name = models.CharField(max_length=50)
    #further break apart the address
    client_address = models.CharField(max_length=100)
    client_phone = PhoneField(blank=True)
    
class Customer(models.Model):
    customer_name = models.CharField(max_length=50)
    #further break apart the address
    client_address = models.CharField(max_length=100)
    client_phone = PhoneField(blank=True)

class Deliverer(models.Model):
    deliverer_name = models.CharField(max_length=50)
    deliverer_phone = PhoneField(blank=True)

class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.PROTECT)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    delivery = models.ForeignKey("Delivery", on_delete=models.PROTECT)
    time_available = models.DateTimeField()

class Delivery(models.Model):
    scheduled_start_time = models.DateTimeField()
    deliverer = models.ForeignKey(Deliverer, on_delete=models.PROTECT)
    delivery_method = models.ForeignKey("DeliveryMethod", on_delete=models.PROTECT)
    total_distance = models.FloatField(default=0)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

class DeliveryMethod(models.Model):
    method_type = models.CharField(max_length=50)
    max_weight = models.IntegerField(default=0)
    max_length = models.IntegerField(default=0)
    max_width = models.IntegerField(default=0)
    max_height = models.IntegerField(default=0)
    max_num_items = models.IntegerField(default=0)

class Specialties(models.Model):
    certification_ID = models.IntegerField(default=0, primary_key=True)
    #this probably should be deleted if the deliverer is deleted
    deliverer = models.ForeignKey(Deliverer, on_delete=models.CASCADE)
    #this probably should be deleted if the method is deleted
    delivery_method = models.ForeignKey(DeliveryMethod, on_delete=models.CASCADE)
    certification_date = models.DateTimeField()
