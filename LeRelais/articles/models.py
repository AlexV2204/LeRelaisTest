from django.db import models


class Articles(models.Model):
    numero = models.IntegerField(default=1)
    page = models.CharField(max_length=20)
    titre = models.CharField(max_length=100)
    texte = models.CharField(max_length=1000)
    image = models.ImageField()