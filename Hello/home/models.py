from django.db import models
# from django.contrib.auth.models import User
# Create your models here.

class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    suubcategory = models.CharField(max_length=50, default="")
    price = models.FloatField(default=0)
    priceone = models.FloatField(default=0)
    pub_date = models.DateField()
    href = models.CharField(max_length=155)
    image = models.ImageField(upload_to='shop/images', default="")

    def __str__(self):
        return self.product_name


class Shop(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    suubcategory = models.CharField(max_length=50, default="")
    price = models.FloatField(default=0)
    priceone = models.FloatField(default=0)
    pub_date = models.DateField()
    image = models.ImageField(upload_to='shop/images', default="")

    def __str__(self):
        return self.product_name

class Homeone(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    suubcategory = models.CharField(max_length=50, default="")
    price = models.FloatField(default=0)
    priceone = models.FloatField(default=0)
    pub_date = models.DateField()
    image = models.ImageField(upload_to='shop/images', default="")

    def __str__(self):
      return self.product_name


class Purification(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    suubcategory = models.CharField(max_length=50, default="")
    price = models.FloatField(default=0)
    priceone = models.FloatField(default=0)
    pub_date = models.DateField()
    image = models.ImageField(upload_to='shop/images', default="")

    def __str__(self):
      return self.product_name


class Drinkware(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    suubcategory = models.CharField(max_length=50, default="")
    price = models.FloatField(default=0)
    priceone = models.FloatField(default=0)
    pub_date = models.DateField()
    image = models.ImageField(upload_to='shop/images', default="")

    def __str__(self):
      return self.product_name
    

class Contact(models.Model):
   name = models.CharField(max_length=155)
   email = models.CharField(max_length=155)
   subject = models.CharField(max_length=155)
   textarea = models.TextField()
   date = models.DateField()


   def __str__(self):
      return self.name


class Corporate(models.Model):
   name = models.CharField(max_length=155)
   phone = models.IntegerField()
   email = models.CharField(max_length=155)
   subject = models.CharField(max_length=155)
   company = models.CharField(max_length=155)
   textarea = models.TextField()
   date = models.DateField()


   def __str__(self):
      return self.name


class Larq(models.Model):
   email = models.CharField(max_length=155)
   date =models.DateField()
   def __str__(self):
      return self.email


class Home(models.Model):
   email = models.CharField(max_length=155)
   date =models.DateField()
   def __str__(self):
      return self.email

class Orders(models.Model):
    # user  = models.ForeignKey(User,on_delete=models.CASCADE)
    order_id = models.AutoField(primary_key=True)
    itemsJson = models.CharField(max_length=5000)
    name = models.CharField(max_length=122)
    lastname = models.CharField(max_length=122)
    username = models.CharField(max_length=122)
    email = models.CharField(max_length=150)
    address = models.CharField(max_length=300)
    address2 = models.CharField(max_length=300)
    country = models.CharField(max_length=300)
    state = models.CharField(max_length=300)
    zip = models.CharField(max_length=300)
    checkbox1 = models.CharField(max_length=300)
    paymentMethod = models.CharField(max_length=300)
    cardname = models.CharField(max_length=300)
    cardnumber = models.CharField(max_length=300)
    expiration = models.CharField(max_length=300)
    cvv = models.CharField(max_length=122)
    date = models.DateField()

    def __str__(self):
        return self.name
class Update(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.TextField(max_length=5000)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7] + "....."
class Tracker(models.Model):
    orderid = models.IntegerField(default="")
    email = models.CharField(max_length=300)

    def __str__(self):
        return self.orderid


class Signup(models.Model):
   username = models.CharField(max_length = 155)
   email = models.CharField(max_length=155)
   password = models.CharField(max_length=155)
   repeatpassword = models.CharField(max_length=155)
   date = models.DateField()

   def __str__(self):
      return self.username

