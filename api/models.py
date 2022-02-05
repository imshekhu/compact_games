from django.db import models
from django.core.validators import MinValueValidator

class Games(models.Model):
    name = models.CharField(max_length=255, unique=True, null=False)
    price = models.FloatField(validators=[MinValueValidator(0.0)])
    space = models.PositiveBigIntegerField()
    
    def __str__(self) :
        return self.name