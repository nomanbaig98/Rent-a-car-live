from django.db import models
from django.contrib import auth
from django.urls import reverse_lazy, reverse
from datetime import datetime
# from django.utils.timezone.now import



class User(auth.models.User, auth.models.PermissionsMixin):

    def __str__(self):
        return "{}".format(self.username)


class Car(models.Model):

    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to='car_images', blank=True)
    daily_rent = models.IntegerField()
    is_available = models.BooleanField()

    def get_absolute_url(self):
        return reverse('car-details', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
           return self.image_url


class Bookings(models.Model):

    car = models.ForeignKey(Car, related_name='car', on_delete=models.CASCADE)
    booking_start_date = models.DateField(default=datetime.now)
    booking_end_date = models.DateField(default=datetime.now)
    is_approved = models.BooleanField(null=True)
    
    # add the username booking






