from django.db import models
from datetime import datetime
from django.core.exceptions import ValidationError


class Personne(models.Model):
    last_name = models.CharField(verbose_name='nom', max_length=200)
    first_name = models.CharField(verbose_name='prénom', max_length=200)
    birthday = models.DateField()

    def save(self, *args, **kwargs):
        if not self.pk:
            if int((datetime.now().date() - self.birthday).days / 365.25) >= 150:
                raise ValidationError("Veuillez mettre un age de moins de 150ans")
        super(Personne, self).save(*args, **kwargs)

    def __str__(self):
        return self.first_name + " " + self.last_name

    @property
    def age(self):
        return int((datetime.now().date() - self.birthday).days / 365.25)
