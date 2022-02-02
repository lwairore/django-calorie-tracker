from calorie_tracker_app.models import ConsumeModel, FoodModel
from django.contrib import admin

# Register your models here.
admin.site.register(FoodModel)

@admin.register(ConsumeModel)
class ConsumeModelAdmin(admin.ModelAdmin):
    list_display = ('user', 'food_consumed',)

