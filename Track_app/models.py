from django.db import models

# Create your models here.

class login(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    usertype = models.CharField(max_length=100)

class category(models.Model):
    category_name = models.CharField(max_length=100)

class user(models.Model):
    name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    pin = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    photo = models.CharField(max_length=100)
    LOGIN = models.ForeignKey(login,on_delete=models.CASCADE,default=1)

class complaint(models.Model):
    complaint = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    reply = models.CharField(max_length=100)
    reply_date = models.CharField(max_length=100)
    USER = models.ForeignKey(user,on_delete=models.CASCADE,default=1)

class store(models.Model):
    store_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    lattitude = models.CharField(max_length=100)
    logitude = models.CharField(max_length=100)
    LOGIN = models.ForeignKey(login, on_delete=models.CASCADE, default=1)

class product(models.Model):
    product_name = models.CharField(max_length=100)
    product_date = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)
    count = models.CharField(max_length=100)
    CATEGORY = models.ForeignKey(category,on_delete=models.CASCADE,default=1)
    STORE = models.ForeignKey(store,on_delete=models.CASCADE,default=1)

class rating(models.Model):
    rating = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    USER = models.ForeignKey(user, on_delete=models.CASCADE, default=1)
    STORE = models.ForeignKey(store, on_delete=models.CASCADE, default=1)

class feedback(models.Model):
    feedback = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    USER = models.ForeignKey(user, on_delete=models.CASCADE, default=1)

class orders(models.Model):
    date = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)
    payment_status = models.CharField(max_length=100)
    STORE = models.ForeignKey(store, on_delete=models.CASCADE, default=1)
    USER = models.ForeignKey(user, on_delete=models.CASCADE, default=1)

class order_sub(models.Model):
    quantity = models.CharField(max_length=100)
    ORDERS = models.ForeignKey(orders, on_delete=models.CASCADE, default=1)
    PRODUCT = models.ForeignKey(product, on_delete=models.CASCADE, default=1)

class cart(models.Model):
    quantity = models.CharField(max_length=100)
    USER = models.ForeignKey(user, on_delete=models.CASCADE, default=1)
    PRODUCT = models.ForeignKey(product, on_delete=models.CASCADE, default=1)



class entry(models.Model):
    entry_date = models.CharField(max_length=100)
    ORDERS = models.ForeignKey(orders, on_delete=models.CASCADE, default=1)

