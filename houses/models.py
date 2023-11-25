from django.db import models

class House(models.Model):

    """Model Definition for Houses"""

    name = models.CharField(max_length=140) # CharField : 길이 제한이 있는 텍스트
    price_per_night = models.PositiveIntegerField()
    description = models.TextField()
    address = models.CharField(max_length=140)
    pet_allowed = models.BooleanField(default=False)