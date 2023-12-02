from django.db import models

class House(models.Model):

    """Model Definition for Houses"""

    name = models.CharField(max_length=140) # CharField : 길이 제한이 있는 텍스트
    price_per_night = models.PositiveIntegerField(verbose_name="Price",
    help_text="Positive integers only")
    description = models.TextField()
    address = models.CharField(max_length=140)
    pets_allowed = models.BooleanField(
        default=False, 
        verbose_name="Pets allowed?",
        help_text="Does this house allow pets?")

    def __str__(self):
        return self.name