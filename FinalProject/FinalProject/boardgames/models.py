from django.db import models

# Create your models here.
class Category(models.Model):
    type = models.CharField(max_length=25)

    def __str__(self):
        return self.type

class Boardgame(models.Model):
    name = models.CharField(max_length=256)
    year_published = models.IntegerField()
    min_players = models.IntegerField()
    max_players = models.IntegerField()
    edition = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name