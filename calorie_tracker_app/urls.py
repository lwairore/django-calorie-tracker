from calorie_tracker_app.apps import CalorieTrackerAppConfig
from django.urls import path
from .views import index,delete_consume

app_name = CalorieTrackerAppConfig.name

urlpatterns = [
    path('', index, name="index"),
    path('delete/<int:id>', delete_consume, name="delete_consume"),
]
