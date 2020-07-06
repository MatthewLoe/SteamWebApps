from django.db import models

# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length=200)
    id = models.IntegerField(primary_key=True)
    discount = models.IntegerField()
    original_price = models.CharField(max_length=200)
    discount_price = models.CharField(max_length=200)

    def __str__(self):
        return self.name
