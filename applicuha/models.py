from datetime import timedelta

from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class CinemaUser(AbstractUser):
    wallet = models.DecimalField(decimal_places=2, max_digits=20, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.wallet = 1000
        super().save(*args, **kwargs)


class Hall(models.Model):
    hall_name = models.CharField(max_length=20)
    places = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.hall_name}'


class MovieInfo(models.Model):
    movie_name = models.CharField(max_length=50)
    movie_time = models.PositiveIntegerField()
    beginning_date = models.DateField()
    ending_date = models.DateField()

    def __str__(self):
        return f'{self.movie_name}'


class Seance(models.Model):
    movie_info = models.ForeignKey(MovieInfo, on_delete=models.CASCADE)
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2, max_digits=20)
    begin_time = models.TimeField()
    end_time = models.TimeField()


class Ticket(models.Model):
    seance = models.ForeignKey(Seance, on_delete=models.CASCADE)
    cinema_user = models.ForeignKey(CinemaUser, on_delete=models.CASCADE)
