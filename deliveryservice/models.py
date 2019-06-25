from django.db import models

class Client(models.Model):
    client_name = models.CharField(max_length=50)
    #further break apart the address
    client_address = models.CharField(max_length=100)
    client_phone = models.IntField(default=0)
    
class Customer(models.Model):
    customer_name = models.CharField(max_length=50)
    #further break apart the address
    client_address = models.CharField(max_length=100)
    #is there a better format for phone number?
    client_phone = models.CharField(max_length=12)

class Deliverer(models.Model):
    deliverer_name = models.CharField(max_length=50)
    #fix phone number field
    deliverer_phone = models.CharField(max_length=12)

class Order(models.Model):
    #is protect the right action to take on delete?
    client = models.ForeignKey(Client, on_delete=models.PROTECT)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    delivery = models.ForeignKey(Delivery, on_delete=models.PROTECT)
    time_available = models.DateTimeField()

class Delivery(models.Model):
    scheduled_start_time = models.DateTimeField()
    deliverer = models.ForeignKey(Deliverer, on_delete=models.PROTECT)
    delivery_method = models.ForeignKey(DeliveryMethod, on_delete=models.PROTECT)
    total_distance = models.FloatField(default=0)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

class DeliveryMethod(models.Model):
    method_type = models.CharField(max_length=50)
    max_weight = models.IntegerField(default=0)
    #make one each for length, width, height
    max_size = models.IntegerField(default=0)
    max_num_items = models.IntegerField(default=0)

class Specialties(models.Model):
    #maybe this should be the primary key rather than the default id added?
    certification_ID = models.IntegerField(default=0)
    #this probably should be deleted if the deliverer is deleted
    deliverer = models.ForeignKey(Deliverer, on_delete=models.CASCADE)
    #this probably should be deleted if the method is deleted
    delivery_method = models.ForeignKey(DeliveryMethod, on_delete=models.CASCADE)
    certification_date = models.DateTimeField()
