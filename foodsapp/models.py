from django.db import models

# Create your models here.

class Food(models.Model):
    name = models.CharField(max_length=200)
    details = models.CharField(max_length=500)
    picture = models.ImageField(upload_to='images/', max_length=100)
    price = models.IntegerField()
    likes = models.IntegerField()
    ordered_times = models.IntegerField()

    def __str__(self):
        return self.name

# class Comment(models.Model):
#     food = models.ForeignKey(Food,on_delete=models.CASCADE)
#     comment_text = models.CharField(max_length=1000)   

# class User(models.Model):
#     username = models.CharField(max_length=200)
#     fullname = models.CharField(max_length=200)
#     address = models.CharField(max_length=200)
#     mobile_number = models.CharField(max_length=200)
#     total_orders = models.IntegerField()
#     favorite_foods = models.CharField(max_length=500)

# class Order(models.Model):
#     user = models.ForeignKey(User, on_delete=models.PROTECT)
#     date = models.DateField('date ordered')
#     checkout = models.BooleanField()
#     value = models.IntegerField()
#     passed  = models.BooleanField()
