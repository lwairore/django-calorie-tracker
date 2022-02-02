from django.db.models import Model
from django.db.models.fields import (CharField, FloatField, IntegerField)

# Create your models here.
class FoodModel(Model):
    
    name = CharField(max_length=100)
    carbs = FloatField()
    protein = FloatField()
    fats = FloatField()
    calories = IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Food'
        verbose_name_plural = 'Foods'
        