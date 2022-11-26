from django.db import models


class Personne(models.Model):
    last_name = models.CharField(verbose_name='nom', max_length=200)
    first_name = models.CharField(verbose_name='prénom', max_length=200)
    birthday = models.DateField()
