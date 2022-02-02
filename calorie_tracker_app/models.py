from django.db.models import Model, ForeignKey, CASCADE
from django.db.models.fields import (CharField, FloatField, IntegerField)
from django.contrib.auth.models import User

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
        
class ConsumeModel(Model):
    user = ForeignKey(User, on_delete=CASCADE)
    food_consumed = ForeignKey(FoodModel, on_delete=CASCADE)

    def __str__(self):
        return f'{self.user.username} {self.food_consumed.name}'

    class Meta:
        verbose_name = 'Consume'
        verbose_name_plural = 'Consumes'
