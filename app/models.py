from django.db import models

import datetime

class Product(models.Model):
    cat_id      = models.ForeignKey(Categories, on_delete= models.CASCADE)
    name        = models.TextField(max_length=200)
    description = models.CharField(max_length=200)
    image       = models.CharField(max_length=200)
    price       = models.DecimalField(max_digits=10,decimal_places=2)
    def __str__(self):
        return self.name


class Categories(models.Model):
    name        = models.TextField(max_length=200)
    description = models.CharField(max_length=200)
    image       = models.CharField(max_length=200)
    def __str__(self):
        return self.name


class Customer(models.Model):
    forename    = models.TextField(max_length=100)
    surname     = models.TextField(max_length=100)
    add1        = models.CharField(max_lentgth=200)
    add2        = models.CharField(max_lentgth=200, blank= True)
    add3        = models.CharField(max_lentgth=200, blank= True)
    postcode    = models.CharField(max_length=50)
    phone       = models.CharField(max_length=50)
    email       = models.CharField(max_length=100)
    registered  = models.BooleanField(default=0)
    def __str__(self):
        return self.name +' '+self.surname


class DeliveryAddresses(models.Model):
    forename    = models.TextField(max_length=100)
    surname     = models.TextField(max_length=100)
    add1        = models.CharField(max_lentgth=200)
    add2        = models.CharField(max_lentgth=200, blank= True)
    add3        = models.CharField(max_lentgth=200, blank= True)
    postcode    = models.CharField(max_length=50)
    phone       = models.CharField(max_length=50)
    email       = models.CharField(max_length=100)
    def __str__(self):
        return self.forename + ' ' + self.surname + ' ' + self.add1

class Orders(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    registered  = models.BooleanField(default=True)
    delivery_add_id= models.ForeignKey(DeliveryAddresses, on_delete=models.CASCADE)
    payment_type= models.CharField(max_length=50)
    date        = models.DateTimeField('time order')
    status      = models.CharField(max_length=50)
    session     = models.CharField(max_length=100)
    total       = models.DecimalField(max_digits=20, decimal_places=2)
    def __str__(self):
        return self.id


class OderItems(models.Model):
    order_id    = models.ForeignKey(Orders, on_delete=models.CASCADE)
    product_id  = models.CharField(max_length=100)
    quantity    = models.IntegerField(default=0)
    def __str__(self):
        return self.order_id + ' ' +self.product_id


class logins(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete= models.CASCADE)
    user_name   = models.CharField(max_length =100)
    password    =models.CharField(max_length =100)


class admin(models.Model):
    user_name   = models.CharField(max_length =100)
    password    =models.CharField(max_length =100)

    
    


    
    

