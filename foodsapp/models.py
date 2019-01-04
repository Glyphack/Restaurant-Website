from django.db import models


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
