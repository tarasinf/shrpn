from django.db import models


class Location(models.Model):
    lat = models.CharField(max_length=25)
    lng = models.CharField(max_length=25)
    address = models.TextField()

    created = models.DateTimeField(auto_now_add=True, auto_now=False)
