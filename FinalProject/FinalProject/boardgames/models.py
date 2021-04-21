from django.db import models

# Create your models here.
class Category(models.Model):
    type = models.CharField(max_length=25)

    def __str__(self):
        return self.type

class Boardgame(models.Model):
    name = models.CharField(max_length=256)
    year_published = models.IntegerField(null=True, blank=True)
    min_players = models.IntegerField(null=True, blank=True)
    max_players = models.IntegerField(null=True, blank=True)
    edition = models.FloatField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

class Player(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Play(models.Model):
    boardgame_id = models.ForeignKey(Boardgame, on_delete=models.CASCADE)
    date = models.DateField(null=True, blank=True)
    winning_player_id = models.ForeignKey(Player, null=True, blank=True, on_delete=models.CASCADE)

class Designer(models.Model):
    name = models.CharField(max_length=48)

    def __str__(self):
        return self.name

class Play_To_Player(models.Model):
    play_id = models.ForeignKey(Play, on_delete=models.CASCADE)
    player_id = models.ForeignKey(Player, on_delete=models.CASCADE)

class Boardgame_Has_Designer(models.Model):
    boardgame_id = models.ForeignKey(Boardgame, on_delete=models.CASCADE)
    designer_id = models.ForeignKey(Designer, on_delete=models.CASCADE)