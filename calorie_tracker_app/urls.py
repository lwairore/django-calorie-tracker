from calorie_tracker_app.apps import CalorieTrackerAppConfig
from django.urls import path
from .views import index

app_name = CalorieTrackerAppConfig.name

urlpatterns = [
    path('', index, name="index"),
]
